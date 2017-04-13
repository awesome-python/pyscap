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
# with documentation at http://www.dmtf.org/sites/default/files/standards/documents/DSP0134_2.6.1.pdf

from scap.collector.cli.WindowsCollector import WindowsCollector
import logging
import ctypes
import ctypes.wintypes
import struct
import uuid

logger = logging.getLogger(__name__)
class SystemUUIDCollector(WindowsCollector):
    def collect(self):
        from scap.collector.cli.windows.WmicCsProductCollector import WmicCsProductCollector
        WmicCsProductCollector(self.host, self.args).collect()
