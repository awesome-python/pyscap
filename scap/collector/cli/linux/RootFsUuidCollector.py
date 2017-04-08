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
import logging

logger = logging.getLogger(__name__)
class RootFsUuidCollector(LinuxCollector):
    def collect(self):
        self.host.facts['root_uuid'] = self.host.exec_command("blkid -o value `mount -l | grep 'on / ' | awk '{print $1}'` | head -n1", sudo=True)[0].strip()
        logger.debug('Root FS UUID: ' + self.host.facts['root_uuid'])
