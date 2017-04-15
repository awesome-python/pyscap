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
class LsbReleaseCollector(LinuxCollector):
    LSB_RELEASE_DISTRIBUTOR_MAP = {
        'RedHatEnterpriseServer': 'redhat'
    }

    def collect(self):
        # TODO convert to a provider collector
        try:
            cpe = CPE(part='o')
            for line in self.host.exec_command('lsb_release -a', sudo=True):
                m = re.match(r'^[^:]+:\s+(.+)$', line)
                if m:
                    name = m.group(1)
                    value = m.group(2)
                    if name == 'Distributor ID':
                        if value in CPECollector.LSB_RELEASE_DISTRIBUTOR_MAP:
                            cpe.set_value('vendor', LsbReleaseCollector.LSB_RELEASE_DISTRIBUTOR_MAP[value])
                    elif name == 'Description':
                        if value.contains('Enterprise Linux Server'):
                            cpe.set_value('product', 'enterprise_linux')
                    elif name == 'Release':
                        cpe.set_value('version', value)
                else:
                    if cpe not in self.host.facts['cpe']['os']:
                        self.host.facts['cpe']['os'].append(cpe)
                    return
        except:
            pass
