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
        if 'network_connections' not in self.host.facts:
            self.host.facts['network_connections'] = {}

        for line in self.host.exec_command('ip route'):
            m = re.match(r'^default via ([0-9.]+) dev\s+([A-Za-z0-9.]+)', line)
            if m:
                route = m.group(1)
                dev = m.group(2)
                if dev not in self.host.facts['network_connections']:
                    self.host.facts['network_connections'][dev] = {}

                logger.debug('default-route: ' + route + ' for device ' + dev)
                self.host.facts['network_connections'][dev]['default_route'] = route
