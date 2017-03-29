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
class NetstatCollector(Collector):
    def collect(self):
        self.host.facts['network_services'] = []
        for line in self.host.lines_from_command('netstat -ln --ip'):
            m = re.match(r'^(tcp|udp)\s+\d+\s+\d+\s+([0-9.]+):([0-9]+)', line)
            if m:
                # NOTE: using tcp|udp as the protocol is in conflict with the ai standard's
                # intent, but since the port #s would not be unique otherwise and it's
                # almost impossible to accurately figure out what the port is being used
                # for, we use tcp & udp instead
                self.host.facts['network_services'].append({'ip_address': m.group(2), 'port': m.group(3), 'protocol': m.group(1)})
