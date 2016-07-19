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

from scap.collector.FactCollector import FactCollector
import re, logging

logger = logging.getLogger(__name__)
class IPRouteCollector(FactCollector):
    def collect_facts(self):
        ip_route = self.host.lines_from_command('ip route')
        logger.debug('ip_route: ' + str(ip_route))
        for line in ip_route:
            m = re.match(r'^default via ([0-9.]+) dev', line)
            if m:
                logger.debug('default-route: ' + m.group(1))
                self.host.facts['default_route'] = m.group(1)
