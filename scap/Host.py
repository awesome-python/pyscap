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

import logging
import inspect
import sys

from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class Host(object):
    @staticmethod
    def load(hostname):
        inventory = Inventory()

        # TODO better connection detection
        if not inventory.has_section(hostname) or not inventory.has_option(hostname, 'connection'):
            if hostname == 'localhost':
                connection_type = 'local'
            else:
                connection_type = 'ssh'
        else:
            connection_type = inventory.get(hostname, 'connection')

        # TODO impacket
        # TODO SMB?
        # TODO PSExec?
        if connection_type == 'ssh':
            from scap.host.cli.SSHHost import SSHHost
            return SSHHost(hostname)
        elif connection_type == 'winrm':
            if not inventory.has_option(hostname, 'winrm_auth_method'):
                raise RuntimeError('Host ' + hostname + ' has not specified option: winrm_auth_method')
            auth_method = inventory.get(hostname, 'winrm_auth_method')
            logger.debug('Using winrm_auth_method ' + auth_method)
            if auth_method == 'ssl':
                from scap.host.cli.winrm.WinRMHostSSL import WinRMHostSSL
                return WinRMHostSSL(hostname)
            elif auth_method == 'ntlm':
                from scap.host.cli.winrm.WinRMHostNTLM import WinRMHostNTLM
                return WinRMHostNTLM(hostname)
            elif auth_method == 'kerberos':
                from scap.host.cli.winrm.WinRMHostKerberos import WinRMHostKerberos
                return WinRMHostKerberos(hostname)
            elif auth_method == 'plaintext':
                from scap.host.cli.winrm.WinRMHostPlaintext import WinRMHostPlaintext
                return WinRMHostPlaintext(hostname)
            else:
                raise RuntimeError('Host ' + hostname + ' specified an invalid winrm_auth_method option')
        elif connection_type == 'local':
            if sys.platform.startswith('linux') or sys.platform == 'cygwin':
                from scap.host.cli.local.LinuxLocalHost import LinuxLocalHost
                return LinuxLocalHost(hostname)
            elif sys.platform == 'win32':
                from scap.host.cli.local.WindowsLocalHost import WindowsLocalHost
                return WindowsLocalHost(hostname)
            else:
                raise NotImplementedError('Local connection on ' + sys.platform + ' is not yet supported')
        else:
            raise RuntimeError('Unsupported host connection type: ' + connection_type)

    def __init__(self, hostname):
        self.hostname = hostname
        self.collectors = []
        self.resources = {}
        self.facts = {}
        self.results = {}

    def connect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def disconnect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def detect_collectors(self, args):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
