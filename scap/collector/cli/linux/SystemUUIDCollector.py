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
        lines = self.host.exec_command('dmidecode --type 1', sudo=True)

        uuid = ''
        for line in lines:
            if "UUID" in line:
                line      = line.replace(" ","")
                pos       = line.find(":")
                uuid = line[pos+1:].strip()

        if not uuid:
            raise RuntimeError('Could not parse system uuid from dmidecode')

        self.host.facts['system_uuid'] = uuid
        logger.debug('System UUID: ' + self.host.facts['system_uuid'])
