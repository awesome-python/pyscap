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
import time

logger = logging.getLogger(__name__)
class NetstatCollector(WindowsCollector):
    VALUE_MAP = {
    }
    def collect(self):
        if 'netstat' in self.host.facts:
            return

        self.host.facts['netstat'] = self.host.exec_command('netstat -n -a')

        if 'network_services' not in self.host.facts:
            self.host.facts['network_services'] = []

        for line in self.host.facts['netstat']:
            # skip blank lines
            if re.match(r'^\s*$', line):
                continue

            if line.startswith('Active Connections'):
                continue

            m = re.match(r'^\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s*$', line)
            if m:
                proto = m.group(1).lower()
                local = m.group(2)
                remote = m.group(3)
                state = m.group(4)
                if state == 'LISTENING':
                    if local.startswith('[::]:'):
                        local_address = '::'
                        local_port = local.replace('[::]:', '')
                    else:
                        local_address, local_port = local.split(':')
                    self.host.facts['network_services'].append({
                        'ip_address': local_address,
                        'port': local_port,
                        'protocol': proto,
                        'source': 'netstat -n -a',
                        'timestamp': time.strftime('%a, %d %b %Y %H:%M:%S %z', time.gmtime()),
                    })
