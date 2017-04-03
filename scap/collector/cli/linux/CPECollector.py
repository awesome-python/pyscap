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
from scap.model.cpe_2_3.CPE import CPE
import re, logging, pprint

logger = logging.getLogger(__name__)
class CPECollector(LinuxCollector):
    def _collect_lshw(self):
        try:
            path = [{}]
            indents = [0]
            for line in self.host.exec_command('lshw', sudo=True):
                m = re.match(r'^([ ]+)\*-(\S+)', line)
                if m:
                    if 'vendor' in path[-1] and 'product' in path[-1] and path[-1]['vendor'] != '000000000000':
                        cpe = CPE(part='h', vendor=path[-1]['vendor'], product=path[-1]['product'])
                        if 'version' in path[-1]:
                            cpe.set_value('version', path[-1]['version'])

                        # we don't add duplicates
                        cpe_uri = cpe.to_uri_string()
                        if cpe_uri not in self.host.facts['cpe']:
                            self.host.facts['cpe'].append(cpe)

                    indent = len(m.group(1))
                    hw_class = m.group(2)
                    cur_indent = indents[-1]
                    if indent > cur_indent:
                        # child; push onto the path
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    elif indent == cur_indent:
                        # sibling; pop then push
                        path.pop()
                        indents.pop()
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    else:
                        # indent < cur_indent
                        # parent; ascend till the indent is equal
                        parent_indent = indents[-1]
                        while parent_indent >= indent:
                            path.pop()
                            indents.pop()
                            parent_indent = indents[-1]
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    continue

                m = re.match(r'^\s+([^:]+): (.*)\s*$', line)
                if m:
                    if m.group(1) == 'configuration':
                        path[-1][m.group(1)] = {}

                        # the below mess is because the values don't escape spaces
                        # so guessing is required
                        keys = []
                        in_key = True
                        (k,v) = ('','')
                        for c in m.group(2):
                            if in_key:
                                if c == '=':
                                    in_key = False
                                elif c == ' ':
                                    # not a key, append to prev value
                                    path[-1][m.group(1)][keys[-1]] += ' ' + k
                                    k = ''
                                else:
                                    k += c
                            else:
                                if c == ' ':
                                    in_key = True
                                    path[-1][m.group(1)][k] = v
                                    keys.append(k)
                                    (k,v) = ('','')
                                else:
                                    v += c
                        path[-1][m.group(1)][k] = v
                    elif m.group(1) == 'capabilities':
                        path[-1][m.group(1)] = m.group(2).split(' ')
                    else:
                        path[-1][m.group(1)] = m.group(2)
        except:
            pass

    def _collect_lspci(self):
        try:
            cpe = CPE(part='h')
            for line in self.host.exec_command('lspci -vmm', sudo=True):
                m = re.match(r'^[^:]+:\s+(.+)$', line)
                if m:
                    name = m.group(1)
                    value = m.group(2)
                    if name == 'Vendor':
                        cpe.set_value('vendor', value)
                    elif name == 'Device':
                        cpe.set_value('product', value)
                    elif name == 'Rev':
                        cpe.set_value('version', value)
                else:
                    cpe_uri = cpe.to_uri_string()
                    if cpe_uri not in self.host.facts['cpe']:
                        self.host.facts['cpe'].append(cpe)
                    cpe = CPE(part='h')
        except:
            pass

    def _collect_lscpu(self):
        try:
            cpe = CPE(part='h')
            for line in self.host.exec_command('lscpu', sudo=True):
                m = re.match(r'^[^:]+:\s+(.+)$', line)
                if m:
                    name = m.group(1)
                    value = m.group(2)
                    if name == 'Vendor ID':
                        cpe.set_value('vendor', value)
                    elif name == 'Model name':
                        cpe.set_value('product', value)
                    elif name == 'CPU family':
                        cpe.set_value('version', value)
                    elif name == 'Model':
                        cpe.set_value('update', value)
                else:
                    cpe_uri = cpe.to_uri_string()
                    if cpe_uri not in self.host.facts['cpe']:
                        self.host.facts['cpe'].append(cpe)
                    cpe = CPE(part='h')
        except:
            pass

    LSB_RELEASE_DISTRIBUTOR_MAP = {
        'RedHatEnterpriseServer': 'redhat'
    }

    def _collect_lsb_release(self):
        try:
            cpe = CPE(part='o')
            for line in self.host.exec_command('lsb_release -a', sudo=True):
                m = re.match(r'^[^:]+:\s+(.+)$', line)
                if m:
                    name = m.group(1)
                    value = m.group(2)
                    if name == 'Distributor ID':
                        if value in CPECollector.LSB_RELEASE_DISTRIBUTOR_MAP:
                            cpe.set_value('vendor', CPECollector.LSB_RELEASE_DISTRIBUTOR_MAP[value])
                    elif name == 'Description':
                        if value.contains('Enterprise Linux Server'):
                            cpe.set_value('product', 'enterprise_linux')
                    elif name == 'Release':
                        cpe.set_value('version', value)
                else:
                    cpe_uri = cpe.to_uri_string()
                    if cpe_uri not in self.host.facts['cpe']:
                        self.host.facts['cpe'].append(cpe)
                    return
        except:
            pass

    def _collect_uname(self):
        try:
            if 'uname' not in self.host.facts:
                from scap.collector.cli.UnameCollector import UnameCollector
                UnameCollector(self.host).collect()
            if self.host.facts['uname'].startswith('Linux'):
                cpe = CPE()
                cpe.set_value('part', 'o')
                cpe.set_value('vendor', 'linux')
                cpe.set_value('product', 'linux_kernel')

                m = re.match(r'^Linux \S+ ([0-9.]+)-(\S+)', self.host.facts['uname'])
                if m:
                    cpe.set_value('version', m.group(1))
                    cpe.set_value('update', m.group(2))
            elif uname.startswith('Darwin'):
                return
            elif uname.startswith('Windows NT'):
                return

            cpe_uri = cpe.to_uri_string()
            if cpe_uri not in self.host.facts['cpe']:
                self.host.facts['cpe'].append(cpe)
        except:
            pass

    def collect(self):
        self.host.facts['cpe'] = []

        # hardware
        self._collect_lshw()
        self._collect_lspci()
        self._collect_lscpu()
        # TODO hwinfo
        # TODO lsusb
        # TODO lsscsi
        # TODO hdparm

        # os
        self._collect_lsb_release()
        self._collect_uname()

        # application
        # TODO rpm -qa

        for cpe in self.host.facts['cpe']:
            logger.debug(cpe.to_uri_string())
