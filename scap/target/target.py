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

import urlparse, logging, inspect
from scap.credential_store import CredentialStore

logger = logging.getLogger(__name__)
class Target(object):
    # TODO move to a config file
    default_scheme = 'ssh'

    @staticmethod
    def parse(spec):
        import ssh_target
        import winrm_target
        if spec.find('://') == -1:
            spec = Target.default_scheme + '://' + spec
        url = urlparse.urlparse(spec)
        if url.scheme == 'ssh':
            creds = CredentialStore()
            if creds.has_section(url.hostname):
                if url.username:
                    creds.set(url.hostname, 'ssh_username', url.username)
                if url.password:
                    creds.set(url.hostname, 'ssh_password', url.password)
            t = ssh_target.SSHTarget(url.hostname, port=(url.port if url.port else 22))
        elif url.scheme == 'winrm':
            #t = winrm_target.WinRMTarget(url.hostname, port=(url.port if url.port else 0))
            raise NotImplementedError('winrm targets are not implemented')
        else:
            logger.critical('Unsupported target scheme: ' + url.scheme)
            sys.exit()
        return t

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def get_hostname(self):
        return self.hostname

    def line_from_command(self, cmd):
        return self.exec_command(cmd).readline()

    def lines_from_command(self, cmd):
        return self.exec_command(cmd).readlines()

    def line_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readline()

    def lines_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readlines()

    def connect(self):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def disconnect(self):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def exec_command(self, cmd):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def can_privileged_command(self):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def exec_privileged_command(self):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def discover_host(self):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
