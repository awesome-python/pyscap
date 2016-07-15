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

from scap.collector.collector import Collector
from scap.model.cpe_2_3.cpe import CPE
import re, logging

logger = logging.getLogger(__name__)
class LinuxCollector(Collector):
    def collect_facts(self):
        # TODO lsb_release -a

        from scap.collector.root_fs_uuid_collector import RootFSUUIDCollector
        self.host.collectors.append(RootFSUUIDCollector(self.host))
        from scap.collector.lshw_collector import LSHWCollector
        self.host.collectors.append(LSHWCollector(self.host))

        # TODO ai.circuit
        # TODO ai.network?; this would likely be  used on routers, switches & other net devices

        # OS CPE
        cpe = CPE()
        cpe.set_value('part', 'o')
        cpe.set_value('vendor', 'linux')
        cpe.set_value('product', 'linux_kernel')

        m = re.match(r'^Linux \S+ ([0-9.]+)-(\S+)', self.host.facts['uname'])
        if m:
            cpe.set_value('version', m.group(1))
            cpe.set_value('update', m.group(2))
        self.host.facts['o_cpe'] = cpe

        from scap.collector.ip_route_collector import IPRouteCollector
        self.host.collectors.append(IPRouteCollector(self.host))

        from scap.collector.hostname_all_fqdns_collector import HostnameAllFQDNsCollector
        self.host.collectors.append(HostnameAllFQDNsCollector(self.host))

        from scap.collector.hostname_collector import HostnameCollector
        self.host.collectors.append(HostnameCollector(self.host))

        from scap.collector.ip_addr_collector import IPAddrCollector
        self.host.collectors.append(IPAddrCollector(self.host))

        from scap.collector.netstat_collector import NetstatCollector
        self.host.collectors.append(NetstatCollector(self.host))

        # TODO ai.database
        # TODO ai.software
            # TODO application CPEs
        # TODO ai.website
