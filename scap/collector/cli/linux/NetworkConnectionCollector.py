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

from scap.collector.cli.LinuxCollector import LinuxCollector
import re, logging

logger = logging.getLogger(__name__)
class NetworkConnectionCollector(LinuxCollector):
    def collect(self):
        from scap.collector.cli.linux.IpAddrCollector import IpAddrCollector
        IpAddrCollector(self.host, self.args).collect()
        from scap.collector.cli.linux.IpRouteCollector import IpRouteCollector
        IpRouteCollector(self.host, self.args).collect()

        for dev, netcon in self.host.facts['network_connections'].items():
            logger.debug('Device: ' + dev)
            if 'mac_address' in netcon:
                logger.debug('MAC: ' + netcon['mac_address'])
            if 'default_route' in netcon:
                logger.debug('Default Route: ' + netcon['default_route'])
            for netadd in netcon['network_addresses']:
                logger.debug('Type: ' + netadd['type'] + ' Address: ' + netadd['address'] + ' Mask: ' + netadd['subnet_mask'])
