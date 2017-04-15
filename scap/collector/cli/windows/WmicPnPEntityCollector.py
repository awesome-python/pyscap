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
class WmicPnPEntityCollector(WindowsCollector):
    VALUE_MAP = {
        'Availability': 'availability',
        'Caption': 'caption',
        'ClassGuid': 'class_guid',
        'CompatibleID': 'compatible_id',
        'ConfigManagerErrorCode': 'config_manager_error_code',
        'ConfigManagerUserConfig': 'config_manager_user_config',
        'CreationClassName': 'creation_class_name',
        'Description': 'description',
        'DeviceID': 'device_id',
        'ErrorCleared': 'error_cleared',
        'ErrorDescription': 'error_description',
        'HardwareID': 'hardware_id',
        'InstallDate': 'install_date',
        'LastErrorCode': 'last_error_code',
        'Manufacturer': 'manufacturer',
        'Name': 'name',
        'PNPDeviceID': 'pnp_device_id',
        'PowerManagementCapabilities': 'power_management_capabilities',
        'PowerManagementSupported': 'power_management_supported',
        'Service': 'service',
        'Status': 'status',
        'StatusInfo': 'status_info',
        'SystemCreationClassName': 'system_creation_class_name',
        'SystemName': 'system_name',
    }
    def collect(self):
        if 'wmic' not in self.host.facts:
            self.host.facts['wmic'] = {}

        if 'pnp_entity' in self.host.facts['wmic']:
            return

        self.host.facts['wmic']['pnp_entity'] = []
        entity = None
        for line in self.host.exec_command('wmic path Win32_PnPEntity get /format:list'):
            line = line.strip()

            # skip blank lines
            if re.match(r'^\s*$', line):
                if entity is None:
                    # preceding blank lines, just skip
                    continue
                else:
                    if len(entity) > 0:
                        # reset the entity
                        self.host.facts['wmic']['pnp_entity'].append(entity)
                        entity = {}
                        continue
                    else:
                        continue
            else:
                if entity is None:
                    entity = {}

            m = re.match(r'^([^=]+)=(.*)$', line)
            if m:
                if m.group(1) in self.VALUE_MAP:
                    name = self.VALUE_MAP[m.group(1)]
                    entity[name] = m.group(2)

        for entity in self.host.facts['wmic']['pnp_entity']:
            cpe = CPE(part='h')

            if entity['manufacturer'] is None or len(entity['manufacturer']) == 0:
                continue
            cpe.set_value('vendor', entity['manufacturer'])
            cpe.set_value('product', entity['name'])

            if cpe not in self.host.facts['cpe']['hardware']:
                self.host.facts['cpe']['hardware'].append(cpe)
