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
class CPECollector(LinuxCollector):
    def _collect_uname(self):
        try:
            if 'uname' not in self.host.facts:
                from scap.collector.cli.UnameCollector import UnameCollector
                UnameCollector(self.host).collect()

            if self.host.facts['uname'].startswith('Linux'):
                cpe = CPE()
                cpe.set_value('part', 'o')
                cpe.set_value('vendor', 'linux')
                cpe.set_value('product', 'linux_kernel')

                m = re.match(r'^Linux \S+ ([0-9.]+)-(\S+)', self.host.facts['uname'])
                if m:
                    cpe.set_value('version', m.group(1))
                    cpe.set_value('update', m.group(2))
            elif uname.startswith('Darwin'):
                return
            elif uname.startswith('Windows NT'):
                return

            if cpe not in self.host.facts['cpe']:
                self.host.facts['cpe'].append(cpe)
        except:
            pass

    def collect(self):
        self.host.facts['cpe'] = []

        # hardware
        from scap.collector.cli.LshwCollector import LshwCollector
        LshwCollector(self.host).collect()

        from scap.collector.cli.LspciCollector import LspciCollector
        LspciCollector(self.host).collect()

        from scap.collector.cli.LscpuCollector import LscpuCollector
        LscpuCollector(self.host).collect()

        # TODO hwinfo
        # TODO lsusb
        # TODO lsscsi
        # TODO hdparm

        # os
        from scap.collector.cli.LsbReleaseCollector import LsbReleaseCollector
        LsbReleaseCollector(self.host).collect()

        self._collect_uname()

        # application
        # TODO rpm -qa

        for cpe in self.host.facts['cpe']:
            logger.debug(cpe.to_uri_string())
