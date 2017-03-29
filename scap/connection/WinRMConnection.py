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

from scap.Connection import Connection
from scap.Inventory import Inventory
from winrm.protocol import Protocol
import logging

logger = logging.getLogger(__name__)
class WinRMConnection(Connection):
    def __init__(self, hostname):
        super(WinRMConnection, self).__init__(hostname)

        self.facts['oval_family'] = 'windows'
        from scap.fact_collector.windows.VerCollector import VerCollector
        self.fact_collectors.append(VerCollector(self))

    def _connect_plaintext(self, address, port):
        inventory = Inventory()

        if inventory.has_option(self.hostname, 'scheme'):
            scheme = inventory.get(self.hostname, 'scheme')
        else:
            scheme = 'http'
        logger.debug('Using url scheme ' + scheme)

        if not inventory.has_option(self.hostname, 'username'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: username')
        username = inventory.get(self.hostname, 'username')
        if inventory.has_option(self.hostname, 'domain'):
            username = inventory.get(self.hostname, 'domain') + '\\' + username
        logger.debug('Using username ' + username)

        if not inventory.has_option(self.hostname, 'password'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: password')
        password = inventory.get(self.hostname, 'password')

        self.protocol = Protocol(
            endpoint=scheme + '://' + address + ':' + port + '/wsman',
            transport='plaintext',
            username=username,
            password=password)

    def _connect_ntlm(self, address, port):
        inventory = Inventory()

        if inventory.has_option(self.hostname, 'scheme'):
            scheme = inventory.get(self.hostname, 'scheme')
        else:
            scheme = 'http'
        logger.debug('Using url scheme ' + scheme)

        if not inventory.has_option(self.hostname, 'username'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: username')
        username = inventory.get(self.hostname, 'username')
        if inventory.has_option(self.hostname, 'domain'):
            username = inventory.get(self.hostname, 'domain') + '\\' + username
        logger.debug('Using username ' + username)

        if not inventory.has_option(self.hostname, 'password'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: password')
        password = inventory.get(self.hostname, 'password')

        self.protocol = Protocol(
            endpoint=scheme + '://' + address + ':' + port + '/wsman',
            transport='ntlm',
            username=username,
            password=password)

    def _connect_kerberos(self, address, port):
        inventory = Inventory()

        if inventory.has_option(self.hostname, 'scheme'):
            scheme = inventory.get(self.hostname, 'scheme')
        else:
            scheme = 'http'
        logger.debug('Using url scheme ' + scheme)

        if not inventory.has_option(self.hostname, 'username'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: username')
        username = inventory.get(self.hostname, 'username')
        if inventory.has_option(self.hostname, 'kerberos_realm'):
            username = username + '@' + inventory.get(self.hostname, 'kerberos_realm')
        logger.debug('Using username ' + username)

        if inventory.has_option(self.hostname, 'kerberos_delegation'):
            kerberos_delegation = inventory.get(self.hostname, 'kerberos_delegation')
        else:
            kerberos_delegation = False

        if inventory.has_option(self.hostname, 'kerberos_hostname_override'):
            kerberos_hostname_override = inventory.get(self.hostname, 'kerberos_hostname_override')
        else:
            kerberos_hostname_override = None
        self.protocol = Protocol(
            endpoint=scheme + '://' + address + ':' + port + '/wsman',
            transport='kerberos',
            username=username,
            kerberos_delegation=kerberos_delegation,
            kerberos_hostname_override=kerberos_hostname_override)

    def _connect_ssl(self, address, port):
        inventory = Inventory()

        if not inventory.has_option(self.hostname, 'cert_pem') and not inventory.has_option(self.hostname, 'cert_key_pem'):
            # try basic auth
            if not inventory.has_option(self.hostname, 'username'):
                raise RuntimeError('Host ' + self.hostname + ' has not specified option: username')
            username = inventory.get(self.hostname, 'username')
            if inventory.has_option(self.hostname, 'domain'):
                username = inventory.get(self.hostname, 'domain') + '\\' + username
            logger.debug('Using username ' + username)

            if not inventory.has_option(self.hostname, 'password'):
                raise RuntimeError('Host ' + self.hostname + ' has not specified option: password')
            password = inventory.get(self.hostname, 'password')

            self.protocol = Protocol(
                endpoint='https://' + address + ':' + port + '/wsman',
                transport='ssl',
                username=username,
                password=password)
        else:
            if not inventory.has_option(self.hostname, 'cert_pem'):
                raise RuntimeError('Host ' + self.hostname + ' has not specified option: cert_pem')
            cert_pem = inventory.get(self.hostname, 'cert_pem')
            if not inventory.has_option(self.hostname, 'cert_key_pem'):
                raise RuntimeError('Host ' + self.hostname + ' has not specified option: cert_key_pem')
            cert_key_pem = inventory.get(self.hostname, 'cert_key_pem')
            if inventory.has_option(self.hostname, 'server_cert_validation'):
                server_cert_validation = inventory.get(self.hostname, 'server_cert_validation')
            else:
                server_cert_validation = 'validate'
            cert_key_pem = inventory.get(self.hostname, 'cert_key_pem')
            self.protocol = Protocol(
                endpoint='https://' + address + ':' + port + '/wsman',
                transport='ssl',
                cert_pem=cert_pem,
                cert_key_pem=cert_key_pem,
                server_cert_validation=server_cert_validation)

    def connect(self):
        inventory = Inventory()

        if inventory.has_option(self.hostname, 'address'):
            address = inventory.get(self.hostname, 'address')
        else:
            address = self.hostname
        logger.debug('Using address ' + address)

        if inventory.has_option(self.hostname, 'port'):
            port = inventory.get(self.hostname, 'port')
        else:
            if inventory.has_option(self.hostname, 'scheme'):
                scheme = inventory.get(self.hostname, 'scheme')
                if scheme == 'http':
                    port = '5985'
                elif scheme == 'https':
                    port = '5986'
                else:
                    raise('Invalid WinRM scheme: ' + scheme)
            else:
                port = '5985'
        logger.debug('Using port ' + port)

        if not inventory.has_option(self.hostname, 'auth_method'):
            raise RuntimeError('Host ' + self.hostname + ' has not specified option: auth_method')
        auth_method = inventory.get(self.hostname, 'auth_method')
        logger.debug('Using auth_method ' + auth_method)
        if auth_method == 'ssl':
            self._connect_ssl(address, port)
        elif auth_method == 'ntlm':
            self._connect_ntlm(address, port)
        elif auth_method == 'kerberos':
            self._connect_kerberos(address, port)
        elif auth_method == 'plaintext':
            self._connect_plaintext(address, port)
        else:
            raise RuntimeError('Host ' + self.hostname + ' specified an invalid auth_method option')

        try:
            self.shell_id = self.protocol.open_shell()
        except Exception as e:
            logger.warning(str(e))

    def disconnect(self):
        self.protocol.close_shell(self.shell_id)

    def exec_command(self, cmd, args):
        if not isinstance(cmd, str) or not isinstance(args, tuple):
            raise RuntimeError('WinRM Host needs a str for a command then args tuple')
        command_id = self.protocol.run_command(self.shell_id, cmd, list(args))
        std_out, std_err, status_code = self.protocol.get_command_output(self.shell_id, command_id)
        self.protocol.cleanup_command(self.shell_id, command_id)

        if status_code != 0:
            raise RuntimeError('Command returned non-zero status code: ' + str(status_code) + ' ' + std_err)
        if std_err:
            raise RuntimeError('Command returned std_err: ' + std_err)

        return std_out.decode()

    def line_from_command(self, cmd, args):
        return self.exec_command(cmd, args).strip('\r\n')

    def lines_from_command(self, cmd, args):
        return self.exec_command(cmd, args).splitlines()
