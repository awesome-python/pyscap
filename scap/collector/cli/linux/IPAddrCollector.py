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

from scap.Collector import Collector
import re, logging

logger = logging.getLogger(__name__)
class IPAddrCollector(Collector):
    def collect(self):
        if 'network_connections' not in self.host.facts:
            self.host.facts['network_connections'] = {}
        for line in self.host.exec_command('ip addr'):
            # index line
            m = re.match(r'^\d+:\s+([A-Za-z0-9.]+):', line)
            if m:
                dev = m.group(1)
                self.host.facts['network_connections'][dev] = {'network_addresses': []}
                continue

            # link line
            m = re.match(r'^\s+link/(ether|loopback) ([:a-f0-9]+)', line)
            if m:
                self.host.facts['network_connections'][dev]['mac_address'] = m.group(2)
                continue

            # inet line
            m = re.match(r'^\s+inet ([0-9.]+)(/\d+)', line)
            if m:
                self.host.facts['network_connections'][dev]['network_addresses'].append({'type': 'ipv4', 'address': m.group(1), 'subnet_mask': m.group(2)})
                continue

            # inet6 line
            m = re.match(r'^\s+inet6 ([0-9:]+)(/\d+)', line)
            if m:
                self.host.facts['network_connections'][dev]['network_addresses'].append({'type': 'ipv6', 'address': m.group(1), 'subnet_mask': m.group(2)})
                continue

        for dev, netcon in self.host.facts['network_connections'].items():
            logger.debug('Device: ' + dev)
            logger.debug('MAC: ' + netcon['mac_address'])
            for netadd in netcon['network_addresses']:
                logger.debug('Type: ' + netadd['type'] + ' Address: ' + netadd['address'] + ' Mask: ' + netadd['subnet_mask'])
