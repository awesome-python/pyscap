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
from scap.model.cpe_2_3.CPE import CPE
import re, logging, pprint

logger = logging.getLogger(__name__)
class LspciCollector(LinuxCollector):
    def collect(self):
        # TODO convert to a provider collector
        try:
            cpe = CPE(part='h')
            for line in self.host.exec_command('lspci -vmm', sudo=True):
                m = re.match(r'^[^:]+:\s+(.+)$', line)
                if m:
                    name = m.group(1)
                    value = m.group(2)
                    if name == 'Vendor':
                        cpe.set_value('vendor', value)
                    elif name == 'Device':
                        cpe.set_value('product', value)
                    elif name == 'Rev':
                        cpe.set_value('version', value)
                else:
                    if cpe not in self.host.facts['cpe']['hardware']:
                        self.host.facts['cpe']['hardware'].append(cpe)
                    cpe = CPE(part='h')
        except:
            pass
