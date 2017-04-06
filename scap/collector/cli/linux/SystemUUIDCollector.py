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

# Based on https://github.com/MyNameIsMeerkat/GetSysUUID/blob/master/GetSysUUID.py

from scap.collector.cli.LinuxCollector import LinuxCollector
import logging

logger = logging.getLogger(__name__)
class SystemUUIDCollector(LinuxCollector):
    def collect(self):
        try:
            from scap.collector.cli.linux.DmiDecodeCollector import DmiDecodeCollector
            DmiDecodeCollector(self.host).collect()
        except:
            # fall back to root fs uuid
            from scap.collector.cli.linux.RootFsUuidCollector import RootFsUuidCollector
            RootFsUuidCollector(self.host).collect()
            self.host.facts['unique_id'] = self.host.facts['root_uuid']
        logger.debug('System UUID: ' + self.host.facts['unique_id'])
