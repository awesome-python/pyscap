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

from scap.host.cli.WinRMHost import WinRMHost
from scap.Inventory import Inventory
from winrm.protocol import Protocol
import logging

logger = logging.getLogger(__name__)
class SSLWinRMHost(WinRMHost):
    def connect(self):
        inventory = Inventory()

        if inventory.has_option(self.hostname, 'address'):
            address = inventory.get(self.hostname, 'address')
        else:
            address = self.hostname
        logger.debug('Using address ' + address)

        if inventory.has_option(self.hostname, 'scheme'):
            scheme = inventory.get(self.hostname, 'scheme')
        else:
            scheme = 'https'
        logger.debug('Using url scheme ' + scheme)

        if inventory.has_option(self.hostname, 'port'):
            port = inventory.get(self.hostname, 'port')
        else:
            if scheme == 'http':
                port = '5985'
            elif scheme == 'https':
                port = '5986'
            else:
                raise('Invalid WinRM scheme: ' + scheme)
        logger.debug('Using port ' + port)

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

        try:
            self.shell_id = self.protocol.open_shell()
        except Exception as e:
            logger.warning(str(e))
