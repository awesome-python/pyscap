#!/usr/bin/env python

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

import xml.etree.ElementTree as ET
import sys, os
from scap.Model import Model

xsd_path = 'ref/oval 5.11.1/Language/schemas/'
# aix-definitions-schema.xsd
# aix-system-characteristics-schema.xsd
# android-definitions-schema.xsd
# android-system-characteristics-schema.xsd
# apache-definitions-schema.xsd
# apache-system-characteristics-schema.xsd
# apple-ios-definitions-schema.xsd
# apple-ios-system-characteristics-schema.xsd
# asa-definitions-schema.xsd
# asa-system-characteristics-schema.xsd
# catos-definitions-schema.xsd
# catos-system-characteristics-schema.xsd
# esx-definitions-schema.xsd
# esx-system-characteristics-schema.xsd
# freebsd-definitions-schema.xsd
# freebsd-system-characteristics-schema.xsd
# hpux-definitions-schema.xsd
# hpux-system-characteristics-schema.xsd
# independent-definitions-schema.xsd
# independent-system-characteristics-schema.xsd
# ios-definitions-schema.xsd
# ios-system-characteristics-schema.xsd
# iosxe-definitions-schema.xsd
# iosxe-system-characteristics-schema.xsd
# junos-definitions-schema.xsd
# junos-system-characteristics-schema.xsd
# linux-definitions-schema.xsd
xsd_path += 'linux-definitions-schema.xsd'
# linux-system-characteristics-schema.xsd
# macos-definitions-schema.xsd
# macos-system-characteristics-schema.xsd
# netconf-definitions-schema.xsd
# netconf-system-characteristics-schema.xsd
# oval-common-schema.xsd
# oval-definitions-schema.xsd
# oval-directives-schema.xsd
# oval-results-schema.xsd
# oval-system-characteristics-schema.xsd
# oval-variables-schema.xsd
# pixos-definitions-schema.xsd
# pixos-system-characteristics-schema.xsd
# sharepoint-definitions-schema.xsd
# sharepoint-system-characteristics-schema.xsd
# solaris-definitions-schema.xsd
# solaris-system-characteristics-schema.xsd
# unix-definitions-schema.xsd
# unix-system-characteristics-schema.xsd
# windows-definitions-schema.xsd
# windows-system-characteristics-schema.xsd
# xmldsig-core-schema.xsd
xsd_namespace = 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux'

module_path = 'scap/model/oval_defs_5_linux'
module_namespace = 'oval_defs_5_linux'

prefix_map = {}
for k,v in Model.NAMESPACES.items():
    ET.register_namespace(v, k)
    prefix_map[v] = k

with open(xsd_path, 'r') as xsd_file:
    root = ET.parse(xsd_file).getroot()
    for el in root.findall('./xsd:element', prefix_map):
        print el.attrib['name']
        if os.path.isfile(module_path + '/' + el.attrib['name'] + '.py'):
            print '  skipping existing ' + el.attrib['name']
            continue
        r = '''# Copyright 2016 Casey Jaymes

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

'''
        if el.attrib['name'].endswith('_test'):
            r += 'from scap.model.' + module_namespace + '.Test import Test\n'
        elif el.attrib['name'].endswith('_state'):
            r += 'from scap.model.' + module_namespace + '.State import State\n'
        elif el.attrib['name'].endswith('_object'):
            r += 'from scap.model.' + module_namespace + '.Object import Object\n'
        else:
            sys.exit('Unknown tag: ' + el.attrib['name'])
        r += '''import logging

logger = logging.getLogger(__name__)
'''
        if el.attrib['name'].endswith('_test'):
            r += 'class ' + el.attrib['name'] + '(Test)\n'
        elif el.attrib['name'].endswith('_state'):
            r += 'class ' + el.attrib['name'] + '(State)\n'
        elif el.attrib['name'].endswith('_object'):
            r += 'class ' + el.attrib['name'] + '(Object)\n'

        r += '    def __init__(self):\n'

        r += '        super(' + el.attrib['name'] + ', self).__init__(\n'
        r += '            \'{' + xsd_namespace + '}' + el.attrib['name'] + '\')\n'
        r += '\n'

        el_els = el.findall('.//xsd:element', prefix_map)
        filtered_el_els = []
        for el_el in el_els:
            if 'ref' in el_el.attrib and (el_el.attrib['ref'] == 'oval-def:set' or el_el.attrib['ref'] == 'oval-def:filter'):
                pass
            elif el.attrib['name'].endswith('_test') and (el_el.attrib['name'] == 'state' or el_el.attrib['name'] == 'object'):
                pass
            else:
                filtered_el_els.append(el_el)
        if len(filtered_el_els) > 0:
            r += '        self.ignore_sub_elements.extend([\n'
            for el_el in filtered_el_els:
                r += '            \'{' + xsd_namespace + '}' + el_el.attrib['name'] + '\',\n'
            r += '        ])\n'

        el_attribs = el.findall('.//xsd:attribute', prefix_map)
        if len(el_attribs) > 0:
            r += '        self.ignore_attributes.extend([\n'
            for el_attrib in el_attribs:
                r += '            \'' + el_attrib.attrib['name'] + '\',\n'
            r += '        ])\n'

        # confirm writing
        print r
        raw_input('Write? ')

        with open(module_path + '/' + el.attrib['name'] + '.py', 'w') as cls_file:
            print >> cls_file, r
