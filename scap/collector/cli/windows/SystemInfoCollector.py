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
class SystemInfoCollector(WindowsCollector):
    SECTION_MAP = {
        'Host Name': 'host_name',
        'OS Name': 'os_name',
        'OS Version': 'os_version',
        'OS Manufacturer': 'os_manufacturer',
        'OS Configuration': 'os_configuration',
        'OS Build Type': 'os_build_type',
        'Registered Owner': 'registered_owner',
        'Registered Organization': 'registered_organization',
        'Product ID': 'product_id',
        'Original Install Date': 'original_install_date',
        'System Boot Time': 'system_boot_time',
        'System Manufacturer': 'system_manufacturer',
        'System Model': 'system_model',
        'System Type': 'system_type',
        'BIOS Version': 'bios_version',
        'Windows Directory': 'windows_directory',
        'System Directory': 'system_directory',
        'Boot Device': 'boot_device',
        'System Locale': 'system_locale',
        'Input Locale': 'input_locale',
        'Time Zone': 'time_zone',
        'Total Physical Memory': 'total_physical_memory',
        'Available Physical Memory': 'available_physical_memory',
        'Domain': 'domain',
        'Logon Server': 'logon_server'
    }

    OS_NAME_MAP = {
        'Microsoft Windows Server 2012': 'cpe:2.3:o:microsoft:windows_server_2012:-:gold:*:*:*:*:*:*',
        'Microsoft Windows Server 2012 R2 Standard': 'cpe:2.3:o:microsoft:windows_server_2012:r2:-:-:*:standard:*:*:*',
        'Microsoft Windows Server 2012 R2 Datacenter': 'cpe:2.3:o:microsoft:windows_server_2012:r2:-:-:*:datacenter:*:*:*',
        'Microsoft Windows Server 2012 R2 Essentials': 'cpe:2.3:o:microsoft:windows_server_2012:r2:-:-:*:essentials:*:*:*'
    }

    def collect(self):
        systeminfo = self.host.exec_command('systeminfo')
        #self.host.facts['_systeminfo_lines'] = systeminfo

        if 'systeminfo' in self.host.facts:
            return
        self.host.facts['systeminfo'] = {}

        multiline = None
        cur_network_card = None
        ip_addresses = False
        for line in systeminfo:
            if re.match(r'^\s*$', line) is not None:
                continue

            if multiline is not None:
                if multiline == 'Processor(s)':
                    m = re.match(r'^\s+\[[0-9]+\]:\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo']['processor'].append(m.group(1))
                        continue

                    multiline = None
                elif multiline == 'Page File Location(s)':
                    m = re.match(r'^\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo']['page_file'].append(m.group(1))
                        continue

                    multiline = None
                elif multiline == 'Hotfix(s)':
                    m = re.match(r'^\s+\[[0-9]+\]:\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo']['hotfix'].append(m.group(1))
                        continue

                    multiline = None
                elif multiline == 'Network Card(s)':
                    if ip_addresses:
                        m = re.match(r'^                                 \[[0-9]+\]:\s+(.*)$', line)
                        if m:
                            self.host.facts['systeminfo']['network_card'][cur_network_card]['IP address(es)'].append(m.group(1))
                            continue
                        else:
                            ip_addresses = False

                    if cur_network_card is not None:
                        m = re.match(r'^                                 (IP address\(es\))\s*$', line)
                        if m:
                            self.host.facts['systeminfo']['network_card'][cur_network_card][m.group(1)] = []
                            ip_addresses = True
                            continue

                        m = re.match(r'^                                 (.+):\s+(.+)$', line)
                        if m:
                            self.host.facts['systeminfo']['network_card'][cur_network_card][m.group(1)] = m.group(2)
                            continue
                        else:
                            cur_network_card = None

                    m = re.match(r'^\s+\[[0-9]+\]:\s+(.*)$', line)
                    if m:
                        self.host.facts['systeminfo']['network_card'][m.group(1)] = {}
                        cur_network_card = m.group(1)
                        continue
                    else:
                        multiline = None
                else:
                    raise RuntimeError('Unknown multiline mode: ' + multiline)

            m = re.match(r'^([^:]+):\s+(.*)$', line)
            if m is None:
                raise RuntimeError('Unexpected line: ' + line)

            if line.startswith('Processor(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo']['processor'] = []
            elif line.startswith('Page File Location(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo']['page_file'] = []
                self.host.facts['systeminfo']['page_file'].append(m.group(2))
            elif line.startswith('Hotfix(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo']['hotfix'] = []
            elif line.startswith('Network Card(s):'):
                multiline = m.group(1)
                self.host.facts['systeminfo']['network_card'] = {}
            elif line.startswith('Virtual Memory:'):
                m = re.match(r'^Virtual Memory: ([^:]+):\s+(.*)$', line)
                if 'virtual_memory' not in self.host.facts['systeminfo']:
                    self.host.facts['systeminfo']['virtual_memory'] = {}

                if m.group(1) == 'Max Size':
                    self.host.facts['systeminfo']['virtual_memory']['max_size'] = m.group(2)
                elif m.group(1) == 'Available':
                    self.host.facts['systeminfo']['virtual_memory']['available'] = m.group(2)
                elif m.group(1) == 'In Use':
                    self.host.facts['systeminfo']['virtual_memory']['in_use'] = m.group(2)
                else:
                    logger.warn('Unknown Virtual Memory section: ' + m.group(1))
            elif line.startswith('Hyper-V Requirements:'):
                #TODO multiline?
                self.host.facts['systeminfo']['hyperv'] = m.group(2)
            elif m.group(1) in SystemInfoCollector.SECTION_MAP:
                self.host.facts['systeminfo'][SystemInfoCollector.SECTION_MAP[m.group(1)]] = m.group(2)
                if m.group(1) == 'OS Name':
                    if m.group(2) in SystemInfoCollector.OS_NAME_MAP:
                        cpe = CPE.from_string(SystemInfoCollector.OS_NAME_MAP[m.group(2)])
                        if cpe not in self.host.facts['cpe']['os']:
                        self.host.facts['cpe']['os'].append(cpe)
                    else:
                        logger.warn('Unable to determine CPE from OS name: ' + m.group(2))
            else:
                logger.warn('Unknown section: ' + m.group(1))
