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

    }
    def collect(self):
        if 'ipconfig' not in self.host.facts:
            self.host.facts['ipconfig'] = {'adapter': []}
        else:
            return

        entry = None
        for line in self.host.exec_command('ipconfig /all'):
            # skip blank lines
            if re.match(r'^\s*$', line):
                continue

            m = re.match(r'^(\S+):$', line)
            if m:
                if m.group(1) == 'Windows IP Configuration':
                    continue
                if entry is not None:
                    self.host.facts['ipconfig']['adapter'].append(entry)
                entry = {'name': m.group(1)}
                continue

            m = re.match(r'^\s+([^.]+)[. ]+: (.*)$', line)
            if m:
                if m.group(1).startswith('Primary Dns Suffix'):
                    self.host.facts['ipconfig']['primary_dns_suffix'] = m.group(2)
                elif m.group(1).startswith('Host Name'):
                    self.host.facts['ipconfig']['host_name'] = m.group(2)

        self.host.facts['ipconfig']['adapter'].append(entry)

        self.host.facts['fqdn'] = [
            self.host.facts['ipconfig']['host_name'] + self.host.facts['ipconfig']['primary_dns_suffix']
        ]
