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
from scap.model.cpe_2_3.CPE import CPE
import re, logging, pprint

logger = logging.getLogger(__name__)
class CPECollector(WindowsCollector):
    def collect(self):
        self.host.facts['cpe'] = {'os', 'application', 'hardware'}

        # hardware
        from scap.collector.cli.windows.WmicPnPEntityCollector import WmicPnPEntityCollector
        WmicPnPEntityCollector(self.host, self.args).collect()

        # os
        from scap.collector.cli.windows.SystemInfoCollector import SystemInfoCollector
        SystemInfoCollector(self.host, self.args).collect()

        # application
        from scap.collector.cli.windows.RegUninstallCollector import RegUninstallCollector
        RegUninstallCollector(self.host, self.args).collect()

        for cpe_part in self.host.facts['cpe']:
            for cpe in self.host.facts['cpe'][cpe_part]
                logger.debug(cpe.to_uri_string())
