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

from scap.FactCollector import FactCollector
from scap.model.cpe_2_3.CPE import CPE
import re, logging

logger = logging.getLogger(__name__)
class UNameCollector(FactCollector):
    def collect(self):
        uname = self.host.line_from_command('uname -a')
        self.host.facts['uname'] = uname
        if uname.startswith('Linux'):
            self.host.facts['oval_family'] = 'unix'
            # TODO lsb_release -a

            from scap.fact_collector.linux.RootFSUUIDCollector import RootFSUUIDCollector
            self.host.fact_collectors.append(RootFSUUIDCollector(self.host))
            #from scap.fact_collector.linux.LSHWCollector import LSHWCollector
            #self.host.fact_collectors.append(LSHWCollector(self.host))

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

            from scap.fact_collector.linux.HostnameAllFQDNsCollector import HostnameAllFQDNsCollector
            self.host.fact_collectors.append(HostnameAllFQDNsCollector(self.host))

            from scap.fact_collector.linux.HostnameCollector import HostnameCollector
            self.host.fact_collectors.append(HostnameCollector(self.host))

            from scap.fact_collector.linux.IPAddrCollector import IPAddrCollector
            self.host.fact_collectors.append(IPAddrCollector(self.host))

            from scap.fact_collector.linux.IPRouteCollector import IPRouteCollector
            self.host.fact_collectors.append(IPRouteCollector(self.host))

            from scap.fact_collector.linux.NetstatCollector import NetstatCollector
            self.host.fact_collectors.append(NetstatCollector(self.host))

            # TODO ai.database
            # TODO ai.software
                # TODO application CPEs
            # TODO ai.website
        elif uname.startswith('Darwin'):
            self.host.facts['oval_family'] = 'macos'
            #/usr/sbin/system_profiler SPHardwareDataType | fgrep 'Serial' | awk '{print $NF}'
            #ioreg -l | awk '/IOPlatformSerialNumber/ { print $4 }' | sed s/\"//g
        elif uname.startswith('Windows NT'):
            #key “MachineGuid” in: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography
            self.host.facts['oval_family'] = 'windows'
        else:
            raise NotImplementedError('Host discovery has not been implemented for uname: ' + uname)
