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
import uuid

logger = logging.getLogger(__name__)
class DmiDecodeCollector(LinuxCollector):
    def collect(self):
        lines = self.host.exec_command('dmidecode --type 1', sudo=True)

        uuid = ''
        for line in lines:
            if "UUID" in line:
                line      = line.replace(" ","")
                pos       = line.find(":")
                u = line[pos+1:].strip()

        if not u:
            raise RuntimeError('Could not parse system uuid from dmidecode')

        u = uuid.UUID(u)
        self.host.facts['unique_id'] = u.hex
        self.host.facts['motherboard_uuid'] = self.host.facts['unique_id']
