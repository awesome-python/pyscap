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

from scap.host.CLIHost import CLIHost
import paramiko.client
import paramiko.pkey
from paramiko.ssh_exception import PasswordRequiredException
import logging
import sys
import binascii
import os
import getpass

from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class SSHHost(CLIHost):
    class AskHostKeyPolicy(paramiko.client.MissingHostKeyPolicy):
        def missing_host_key(self, client, hostname, key):
            fpt = key.get_fingerprint()
            logger.debug('Fingerprint: ' + str(fpt))
            hex_fpt = str(binascii.hexlify(fpt), encoding='utf-8')
            logger.debug('Hex Fingerprint: ' + hex_fpt)
            response = input('Accept key ' + hex_fpt + ' for host ' + hostname + ' (Y/n)? ')
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

    def __init__(self, hostname):
        super(SSHHost, self).__init__(hostname)

        from scap.collector.cli.unix.UNameCollector import UNameCollector
        self.collectors.append(UNameCollector(self))

    def connect(self):
        self.client = paramiko.client.SSHClient()
        self.client.load_system_host_keys()
        try:
            # TODO windows/linux home instead of ~
            logger.debug('Read ssh host keys from ~/.pyscap/ssh_host_keys')
            self.client.load_host_keys(os.path.expanduser('~/.pyscap/ssh_host_keys'))
        except:
            logger.warning("Couldn't read ssh host keys")
        self.client.set_missing_host_key_policy(self.AskHostKeyPolicy())

        inventory = Inventory()

        if inventory.has_option(self.hostname, 'ssh_port'):
            port = inventory.get(self.hostname, 'ssh_port')
        else:
            port = 22

        self.sudo_password = None

        if inventory.has_option(self.hostname, 'ssh_username') and inventory.has_option(self.hostname, 'ssh_password'):
            self.client.connect(self.hostname, port=port,
                username=inventory.get(self.hostname, 'ssh_username'),
                password=inventory.get(self.hostname, 'ssh_password'))
            if inventory.has_option(self.hostname, 'sudo_password'):
                self.sudo_password = inventory.get(self.hostname, 'sudo_password')
            else:
                self.sudo_password = inventory.get(self.hostname, 'ssh_password')
        elif inventory.has_option(self.hostname, 'ssh_private_key_filename'):
            if inventory.has_option(self.hostname, 'ssh_private_key_file_password'):
                self.client.connect(self.hostname, port=port,
                    key_filename=inventory.get(self.hostname, 'ssh_private_key_filename'),
                    password=inventory.get(self.hostname, 'ssh_private_key_file_password'))
            else:
                try:
                    self.client.connect(self.hostname, port=port,
                        key_filename=inventory.get(self.hostname, 'ssh_private_key_filename'))
                except PasswordRequiredException:
                    # retry with password
                    ssh_private_key_file_password = getpass.getpass('Password for private key file ' +
                        inventory.get(self.hostname, 'ssh_private_key_filename') + ': ')
                    self.client.connect(self.hostname, port=port,
                        key_filename=inventory.get(self.hostname, 'ssh_private_key_filename'),
                        password=ssh_private_key_file_password)
        else:
            ssh_username = input('Username for host ' + self.hostname + ': ')
            if ssh_username.strip() == '':
                raise RuntimeError('No method of authenticating with host ' + self.hostname + ' found')
            ssh_password = getpass.getpass('Password for host ' + self.hostname + ': ')
            if inventory.has_option(self.hostname, 'sudo_password'):
                self.sudo_password = inventory.get(self.hostname, 'sudo_password')
            else:
                self.sudo_password = ssh_password
            self.client.connect(self.hostname, port=port, username=ssh_username, password=ssh_password)

    def exec_command(self, cmd, sudo=False, enable=False):
        inventory = Inventory()
        if sudo:
            if not self.sudo_password:
                if not inventory.has_option(self.hostname, 'sudo_password'):
                    self.sudo_password = getpass.getpass('Sudo password for host ' + self.hostname + ': ')
                else:
                    self.sudo_password = inventory.get(self.hostname, 'sudo_password')
            cmd = 'sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"'
        elif enable:
            if not self.enable_password:
                if not inventory.has_option(self.hostname, 'enable_password'):
                    self.enable_password = getpass.getpass('Enable password for host ' + self.hostname + ': ')
                else:
                    self.enable_password = inventory.get(self.hostname, 'enable_password')

        else:
            cmd = 'sh -c "' + cmd.replace('"', r'\"') + '"'

        logger.debug("Sending command: " + cmd)
        stdin, stdout, stderr = self.client.exec_command(cmd)

        if sudo:
            logger.debug("Sending sudo_password...")
            stdin.write(self.sudo_password + "\n")
            # eat the prompt
            stderr.readline()

        err = stderr.read()
        if err.strip():
            raise RuntimeError(err)
        return stdout.readlines()

    def disconnect(self):
        self.client.close()
