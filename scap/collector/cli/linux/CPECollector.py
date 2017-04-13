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
    def collect(self):
        self.host.facts['cpe'] = []

        # hardware
        from scap.collector.cli.linux.LshwCollector import LshwCollector
        LshwCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.LspciCollector import LspciCollector
        LspciCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.LscpuCollector import LscpuCollector
        LscpuCollector(self.host, self.args).collect()

        # TODO hwinfo
        # TODO lsusb
        # TODO lsscsi
        # TODO hdparm

        # os
        from scap.collector.cli.linux.LsbReleaseCollector import LsbReleaseCollector
        LsbReleaseCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.UNameCollector import UNameCollector
        UNameCollector(self.host, self.args).collect()

        # application
        # TODO rpm -qa

        for cpe in self.host.facts['cpe']:
            logger.debug(cpe.to_uri_string())
