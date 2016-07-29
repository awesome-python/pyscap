# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

from scap.Host import Host
import paramiko.client, logging, sys, binascii, os
from scap.CredentialStore import CredentialStore

logger = logging.getLogger(__name__)
class SSHHost(Host):
    class AskHostKeyPolicy(paramiko.client.MissingHostKeyPolicy):
        def missing_host_key(self, client, hostname, key):
            response = raw_input('Accept key ' + binascii.hexlify(key.get_fingerprint()) + ' for host ' + hostname + ' (Y/n)? ')
            if response == '' or response.lower()[0] == 'y':
                logger.debug('Adding key for host ' + hostname)
                host_keys = client.get_host_keys()
                host_keys.add(hostname, key.get_name(), key)
                if not os.path.exists(os.path.expanduser('~/.pyscap')):
                    try:
                        os.mkdir(os.path.expanduser('~/.pyscap'))
                        logger.debug('Created ~/.pyscap')
                    except:
                        logger.warning('Could not create directory ~/.pyscap')
                        return
                try:
                    host_keys.save(os.path.expanduser('~/.pyscap/ssh_host_keys'))
                    logger.debug('Saved ~/.pyscap/ssh_host_keys')
                except:
                    logger.warning("Couldn't save ssh host keys")
                return
            else:
                raise RuntimeError('Key for ' + hostname + ' not accepted')

    def __init__(self, hostname, port):
        super(SSHHost, self).__init__(hostname, port)

        from scap.fact_collector.UNameCollector import UNameCollector
        self.fact_collectors.append(UNameCollector(self))

        creds = CredentialStore()
        if not creds.has_section(hostname):
            logger.critical('No credentials defined for host ' + hostname)
            sys.exit()

    def connect(self):
        self.client = paramiko.client.SSHClient()
        self.client.load_system_host_keys()
        try:
            self.client.load_host_keys(os.path.expanduser('~/.pyscap/ssh_host_keys'))
            logger.debug('Read ssh host keys from ~/.pyscap/ssh_host_keys')
        except:
            logger.warning("Couldn't read ssh host keys")
        self.client.set_missing_host_key_policy(self.AskHostKeyPolicy())
        creds = CredentialStore()
        if creds.has_option(self.hostname, 'ssh_private_key'):
            self.client.connect(self.hostname, port=self.port,
                pkey=creds.get(self.hostname, 'ssh_private_key'))
        elif creds.has_option(self.hostname, 'ssh_username') and creds.has_option(self.hostname, 'ssh_password'):
            self.client.connect(self.hostname, port=self.port,
                username=creds.get(self.hostname, 'ssh_username'),
                password=creds.get(self.hostname, 'ssh_password'))
        elif creds.has_option(self.hostname, 'ssh_private_key_filename'):
            self.client.connect(self.hostname, port=self.port,
                key_filename=creds.get(self.hostname, 'ssh_private_key_filename'))
        else:
            raise RuntimeError('No method of authenticating with host ' + self.hostname + ' found')

    def exec_command(self, cmd):
        logger.debug("Sending command: " + 'sh -c "' + cmd.replace('"', r'\"') + '"')
        stdin, stdout, stderr = self.client.exec_command('sh -c "' + cmd.replace('"', r'\"') + '"')

        err = stderr.read()
        if err.strip():
            raise RuntimeError(err)
        return stdout

    def can_privileged_command(self):
        creds = CredentialStore()
        return creds.has_option(self.hostname, 'sudo_password')

    def exec_privileged_command(self, cmd):
        creds = CredentialStore()
        if not creds.has_option(self.hostname, 'sudo_password'):
            raise RuntimeError("Can't run privileged command without sudo_password defined in credentials")
        logger.debug("Sending command: " + 'sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"')
        stdin, stdout, stderr = self.client.exec_command('sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"')

        logger.debug("Sending sudo_password...")
        stdin.write(creds.get(self.hostname, 'sudo_password') + "\n")
        # eat the prompt
        stderr.readline()

        err = stderr.read()
        if err.strip():
            raise RuntimeError(err)
        return stdout

    def disconnect(self):
        self.client.close()
