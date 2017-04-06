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

from scap.collector.cli.WindowsCollector import WindowsCollector
import logging
import re
from scap.model.cpe_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class IpConfigAllCollector(WindowsCollector):
    VALUE_MAP = {
        'Primary Dns Suffix': 'primary_dns_suffix',
        'Host Name': 'ipconfig_all_hostname',
        'Node Type': 'ipconfig_all_node_type',
        'IP Routing Enabled': 'ip_routing_enabled',
        'WINS Proxy Enabled': 'wins_proxy_enabled',
        'DNS Suffix Search List': 'dns_suffix',
        'Description': 'description',
        'Physical Address': 'mac_address',
        'DHCP Enabled': 'dhcp_enabled',
        'Autoconfiguration Enabled': 'autoconfiguration_enabled',
        'Link-local IPv6 Address': 'link_local_ipv6_address',
        'IPv4 Address': 'ipv4_address',
        'Subnet Mask': 'subnet_mask',
        'Lease Obtained': 'lease_obtained',
        'Lease Expires': 'lease_expires',
        'Default Gateway': 'default_gateway',
        'DHCP Server': 'dhcp_server',
        'DHCPv6 IAID': 'dhcpv6_iaid',
        'DHCPv6 Client DUID': 'dhcpv6_client_duid',
        'DNS Servers': 'dns_server',
        'NetBIOS over Tcpip': 'netbios_over_tcpip',
        'Connection-specific DNS Suffix': 'connection_dns_suffix',
        'Media State': 'media_state',
    }
    def collect(self):
        if 'ipconfig_all' in self.host.facts:
            return

        self.host.facts['ipconfig_all'] = self.host.exec_command('ipconfig /all')

        if 'network_connections' not in self.host.facts:
            self.host.facts['network_connections'] = {}

        dev = None
        last_name = None
        for line in self.host.facts['ipconfig_all']:
            # skip blank lines
            if re.match(r'^\s*$', line):
                continue

            if line.startswith('Windows IP Configuration'):
                continue

            m = re.match(r'^(\S+) adapter (\S+):\s*$', line)
            if m:
                type_ = m.group(1)
                dev = m.group(2)
                if dev not in self.host.facts['network_connections']:
                    self.host.facts['network_connections'][dev] = {'type': type_}
                continue

            m = re.match(r'^\s+([^.]+)[. ]+: (.*)$', line)
            if m:
                name = m.group(1).strip()
                if name in self.VALUE_MAP:
                    name = self.VALUE_MAP[name]
                else:
                    logger.debug('Found unrecognized name in ipconfig: ' + name)
                    continue
                last_name = name
                value = m.group(2)
                if dev is None:
                    # still in Windows IP Configuration
                    self.host.facts[name] = value
                else:
                    self.host.facts['network_connections'][dev][name] = value
                continue

            m = re.match(r'^\s+([^:]+)$', line)
            if m:
                value = m.group(1)
                if dev is None:
                    # still in Windows IP Configuration
                    if isinstance(self.host.facts[last_name], list):
                        self.host.facts[last_name].append(value)
                    else:
                        self.host.facts[last_name] = [self.host.facts[last_name]]
                else:
                    if isinstance(self.host.facts['network_connections'][dev][last_name], list):
                        self.host.facts['network_connections'][dev][last_name].append(value)
                    else:
                        self.host.facts['network_connections'][dev][last_name] = [self.host.facts['network_connections'][dev][last_name]]
            else:
                logger.debug('Unmatched line: ' + line)

        for dev, netcon in self.host.facts['network_connections'].items():
            self.host.facts['network_connections'][dev]['network_addresses'] = []
            if 'link_local_ipv6_address' in netcon:
                self.host.facts['network_connections'][dev]['network_addresses'].append({
                    'type': 'ipv6',
                    'address': netcon['link_local_ipv6_address'].replace(' (Preferred)', ''),
                    'subnet_mask': '/126',
                })
            if 'ipv4_address' in netcon and 'subnet_mask' in netcon:
                self.host.facts['network_connections'][dev]['network_addresses'].append({
                    'type': 'ipv4',
                    'address': netcon['ipv4_address'].replace(' (Preferred)', ''),
                    'subnet_mask': netcon['subnet_mask'],
                })
        self.host.facts['fqdn'] = [
            self.host.facts['ipconfig_all_hostname'] + self.host.facts['primary_dns_suffix']
        ]
