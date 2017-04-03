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

from scap.Collector import Collector
import logging
import ctypes
import ctypes.wintypes
import struct

logger = logging.getLogger(__name__)
class SystemUUIDCollector(Collector):
    #FirmwareTableSig = ord('R')
    #FirmwareTableSig = FirmwareTableSig << 8 | ord("S")
    #FirmwareTableSig = FirmwareTableSig << 8 | ord("M")
    #FirmwareTableSig = FirmwareTableSig << 8 | ord("B")
    RSMB = 1381190978   # 'RSMB'

    def collect(self):
        # figure out the size of the table
        bios_size = ctypes.windll.kernel32.GetSystemFirmwareTable(ctypes.wintypes.DWORD(SystemUUIDCollector.RSMB), 0, 0, 0)

        # allocate a buffer
        buf = ctypes.create_string_buffer("\000"*bios_size)

        # pull the actual table
        ret = ctypes.windll.kernel32.GetSystemFirmwareTable(ctypes.wintypes.DWORD(SystemUUIDCollector.RSMB), 0, buf, 0x1eba)

        if ctypes.GetLastError() != 0:
            raise RuntimeError('Could not pull system firmware table')

        # remove the 8 byte header MS seems to append
        buf = buf.raw[8:]
        self.host.facts['system_uuid'] =
        logger.debug('System UUID: ' + self.host.facts['system_uuid'])
