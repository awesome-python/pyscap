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
import logging
import re
from scap.model.cpe_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class WmicCsProductCollector(WindowsCollector):
    VALUE_MAP = {
        'Description': 'description',
        'IdentifyingNumber': 'identifying_number',
        'Name': 'name',
        'SKUNumber': 'sku_number',
        'UUID': 'uuid',
        'Vendor': 'vendor',
        'Version': 'version',
    }
    def collect(self):
        if 'wmic' not in self.host.facts:
            self.host.facts['wmic'] = {}

        self.host.facts['wmic']['csproduct'] = {}

        for line in self.host.exec_command('wmic csproduct list full'):
            line = line.strip()

            # skip blank lines
            if line == '':
                continue

            m = re.match(r'^([^=]+)=(.*)$', line)
            if m:
                if m.group(1) in self.VALUE_MAP:
                    name = self.VALUE_MAP[m.group(1)]
                    self.host.facts['wmic']['csproduct'][name] = m.group(2)

                    # Description=Computer System Product
                    # IdentifyingNumber=VMware-12 34 56 78 90 12 34 56-78 90 12 34 56 78 90 12
                    # Name=VMware Virtual Platform
                    # SKUNumber=
                    # UUID=12345678-1234-1234-1234-123456789012
                    if name == 'uuid':
                        self.host.facts['system_uuid'] = m.group(2)
                    # Vendor=VMware, Inc.
                    # Version=None
