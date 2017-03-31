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
from scap.Inventory import Inventory
from smb.SMBHost import SMBHost
from nmb.NetBIOS import NetBIOS
import string, random, socket, logging

logger = logging.getLogger(__name__)
class SMBHost(Host):
    def __init__(self, hostname, args = {}):
        super(SMBHost, self).__init__(hostname, args)

        # TODO initialize collectors

    def connect(self):
        inventory = Inventory()
        address = self.hostname
        if inventory.has_option(self.hostname, 'address'):
            address = inventory.get(self.hostname, 'address')

        ip = None
        nb_name = None
        try:
            socket.inet_aton(address)
            ip = address
        except OSError as e:
            nb_name = address

        nb = NetBIOS()
        if ip is not None and nb_name is None:
            # need to look up the hostname
            logger.debug('Looking up NetBIOS name from IP ' + ip)
            nb_names = nb.queryIPForName(ip)
            if nb_names is None or len(nb_names) < 1:
                raise RuntimeError('Cannot connect to host ' + self.hostname + '; looking up NetBIOS name failed')
            nb_name = nb_names[0]
        elif ip is None and nb_name is not None:
            # not a IPv4 address, need to look up the ip
            nb_name = address
            logger.debug('Looking up NetBIOS IP from name ' + nb_name)
            ips = nb.queryName(nb_name)
            if ips is None or len(ips) < 1:
                raise RuntimeError('Cannot connect to host ' + self.hostname + '; looking up NetBIOS IP failed')
            ip = ips[0]
        nb.close()

        if inventory.has_option(self.hostname, 'username') and inventory.has_option(self.hostname, 'password'):
            username = inventory.get(self.hostname, 'username')
            password = inventory.get(self.hostname, 'password')
            client_machine_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
            logger.debug('Using client name of ' + client_machine_name)
            logger.info('Connecting to ' + nb_name + ' as ' + username + ' for host ' + self.hostname)
            self.connection = SMBHost(username, password, client_machine_name, nb_name, use_ntlm_v2 = True, sign_options=SMBHost.SIGN_WHEN_SUPPORTED)#, is_direct_tcp=True)
            if not self.connection.connect(ip):
                raise RuntimeError('Cannot connect to host ' + self.hostname + '; connecting via SMB failed')
        else:
            raise RuntimeError('No method of authenticating with host ' + self.hostname + ' found')

        print(str(self.connection.listPath('ADMIN$', '\\')))

    def disconnect(self):
        self.connection.close()
