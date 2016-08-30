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
import logging
import re

logger = logging.getLogger(__name__)
class SystemInfoCollector(FactCollector):
    def collect(self):
        systeminfo = self.host.lines_from_command('systeminfo', ())
        #self.host.facts['_systeminfo_lines'] = systeminfo

        self.host.facts['systeminfo'] = {}

        multiline = None
        cur_network_card = None
        ip_addresses = False
        for line in systeminfo:
            if re.match(r'^\s*$', line) is not None:
                continue

            if multiline is not None:
                if multiline == 'Processor(s)':
                    m = re.match(r'^\s+\[[0-9]+\]:\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo'][multiline].append(m.group(1))
                        continue

                    multiline = None
                elif multiline == 'Page File Location(s)':
                    m = re.match(r'^\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo'][multiline].append(m.group(1))
                        continue

                    multiline = None
                elif multiline == 'Hotfix(s)':
                    m = re.match(r'^\s+\[[0-9]+\]:\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo'][multiline].append(m.group(1))
                        continue

                    multiline = None
                elif multiline == 'Network Card(s)':
                    if ip_addresses:
                        m = re.match(r'^                                 \[[0-9]+\]:\s+(.*)$', line)
                        if m:
                            self.host.facts['systeminfo'][multiline][cur_network_card]['IP address(es)'].append(m.group(1))
                            continue
                        else:
                            ip_addresses = False

                    if cur_network_card is not None:
                        m = re.match(r'^                                 (IP address\(es\))\s*$', line)
                        if m:
                            self.host.facts['systeminfo'][multiline][cur_network_card][m.group(1)] = []
                            ip_addresses = True
                            continue

                        m = re.match(r'^                                 (.+):\s+(.+)$', line)
                        if m:
                            self.host.facts['systeminfo'][multiline][cur_network_card][m.group(1)] = m.group(2)
                            continue
                        else:
                            cur_network_card = None

                    m = re.match(r'^\s+\[[0-9]+\]:\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo'][multiline][m.group(1)] = {}
                        cur_network_card = m.group(1)
                        continue
                    else:
                        multiline = None
                else:
                    raise RuntimeError('Unknown multiline mode: ' + multiline)

            m = re.match(r'^([^:]+):\s+(.*)$', line)
            if m is None:
                raise RuntimeError('Unexpected line: ' + line)

            if line.startswith('Processor(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo'][m.group(1)] = []
            elif line.startswith('Page File Location(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo'][m.group(1)] = []
                self.host.facts['systeminfo'][multiline].append(m.group(2))
            elif line.startswith('Hotfix(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo'][m.group(1)] = []
            elif line.startswith('Network Card(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo'][m.group(1)] = {}
            elif line.startswith('Virtual Memory:'):
                m = re.match(r'^Virtual Memory: ([^:]+):\s+(.*)$', line)
                self.host.facts['systeminfo']['Virtual Memory: ' + m.group(1)] = m.group(2)
            elif line.startswith('Hyper-V Requirements:'):
                #TODO multiline?
                self.host.facts['systeminfo'][m.group(1)] = m.group(2)
            else:
                self.host.facts['systeminfo'][m.group(1)] = m.group(2)
