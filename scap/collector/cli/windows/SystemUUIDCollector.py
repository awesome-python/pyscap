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

from scap.collector.cli.WindowsCollector import WindowsCollector
import logging
import ctypes
import ctypes.wintypes
import struct
import uuid

logger = logging.getLogger(__name__)
class SystemUUIDCollector(WindowsCollector):
    # RSMB = ord('R')
    # RSMB = RSMB << 8 | ord("S")
    # RSMB = RSMB << 8 | ord("M")
    # RSMB = RSMB << 8 | ord("B")
    RSMB = 1381190978   # 'RSMB'
    STRUCTURE_TYPES = {
        0: 'BIOS Information',
        1: 'System Information',
        2: 'Base Board (or Module) Information',
        3: 'System Enclosure',
        4: 'Processor Information',
        5: 'Memory Controller Information',
        6: 'Memory Module Information',
        7: 'Cache Information',
        8: 'Port Connector Information',
        9: 'System Slots',
        10: 'On Board Devices Information',
        11: 'OEM Strings',
        12: 'System Configuration Options',
        13: 'BIOS Language Information',
        14: 'Group Associations',
        15: 'System Event Log',
        16: 'Physical Memory Array',
        17: 'Memory Device',
        18: '32-bit Memory Error Information',
        19: 'Memory Array Mapped Address',
        20: 'Memory Device Mapped Address',
        21: 'Built-in Pointing Device',
        22: 'Portable Battery',
        23: 'System Reset',
        24: 'Hardware Security',
        25: 'System Power Controls',
        26: 'Voltage Probe',
        27: 'Cooling Device',
        28: 'Temperature Probe',
        29: 'Electrical Current Probe',
        30: 'Out-of-Band Remote Access',
        31: 'Boot Integrity Services (BIS) Entry Point',
        32: 'System Boot Information',
        33: '64-bit Memory Error Information',
        34: 'Management Device',
        35: 'Management Device Component',
        36: 'Management Device Threshold Data',
        37: 'Memory Channel',
        38: 'IPMI Device Information',
        39: 'System Power Supply',
        40: 'Additional Information',
        41: 'Onboard Devices Extended Information',
        126: 'Inactive',
        127: 'End-of-Table'
    }
    def collect(self):
        # figure out the size of the table
        bios_size = ctypes.windll.kernel32.GetSystemFirmwareTable(ctypes.wintypes.DWORD(SystemUUIDCollector.RSMB), 0, 0, 0)
        #logger.debug('bios_size: ' + str(bios_size))

        # allocate a buffer
        buf = ctypes.create_string_buffer(b'\000' * bios_size)

        # pull the actual table
        ret = ctypes.windll.kernel32.GetSystemFirmwareTable(ctypes.wintypes.DWORD(SystemUUIDCollector.RSMB), 0, buf, bios_size)
        if ctypes.GetLastError() != 0:
            raise RuntimeError('Could not pull system firmware table: ' + str(ctypes.GetLastError()))

        # remove the 8 byte header MS seems to append
        buf = buf.raw
        #buf = buf.raw[8:]

        Used20CallingMethod, SMBIOSMajorVersion, SMBIOSMinorVersion, DmiRevision, Length = struct.unpack("<BBBBL", buf[0:8])
        #logger.debug('Used20CallingMethod, SMBIOSMajorVersion, SMBIOSMinorVersion, DmiRevision, Length: ' + str([Used20CallingMethod, SMBIOSMajorVersion, SMBIOSMinorVersion, DmiRevision, Length]))
        buf = buf[8:]
        #logger.debug(str(buf))

        while 1:
            try:
                type_, formatted_len, handle = struct.unpack("<BBH", buf[0:4])
                #logger.debug('type_, formatted_len, handle: ' + str([type_, formatted_len, handle]))
            except IndexError:
                ##Reached the end of the structure
                break

            if type_ in SystemUUIDCollector.STRUCTURE_TYPES:
                pass
                #logger.debug(SystemUUIDCollector.STRUCTURE_TYPES[type_] + ' structure')
            else:
                raise NotImplementedError('SMBIOS structure type ' + str(type_) + ' is not implemented')

            if type_ == 1: # System Information
                mfg, prod, vers, serial, u, wakeup, sku, family = struct.unpack("<BBBB16sBBB", buf[4:27])
                u = uuid.UUID(bytes_le=u)
                logger.debug('uuid: ' + u.hex)
                self.host.facts['system_uuid'] = u.hex
            elif type_ == 127: # End-of-Table
                break

            buf = buf[formatted_len:]

            unformatted_len = buf.find(b'\000\000') + 2
            buf = buf[unformatted_len:]

        #self.host.facts['system_uuid'] =
        logger.debug('System UUID: ' + self.host.facts['system_uuid'])
