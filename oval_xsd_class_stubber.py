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

if len(sys.argv) < 3:
    sys.exit('Usage: ' + sys.argv[0] + ' xsd.xml dir/to/put/modules')

prefix_map = {}
for k,v in Model.namespaces.items():
    ET.register_namespace(v, k)
    prefix_map[v] = k

with open(sys.argv[1], 'r') as xsd_file:
    root = ET.parse(xsd_file).getroot()
    for el in root.findall('./xsd:element', prefix_map):
        print el.attrib['name']
        if os.path.isfile(sys.argv[2] + '/' + el.attrib['name'] + '.py'):
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
            r += 'from scap.model.oval_defs_5.Test import Test\n'
        elif el.attrib['name'].endswith('_state'):
            r += 'from scap.model.oval_defs_5.State import State\n'
        elif el.attrib['name'].endswith('_object'):
            r += 'from scap.model.oval_defs_5.Object import Object\n'
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
        r += '            \'{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}' + el.attrib['name'] + '\')\n'
        r += '\n'

        el_els = el.findall('.//xsd:element', prefix_map)
        filtered_el_els = []
        for el_el in el_els:
            if 'ref' in el_el.attrib and (el_el.attrib['ref'] == 'oval-def:set' or el_el.attrib['ref'] == 'oval-def:filter'):
                pass
            else:
                filtered_el_els.append(el_el)
        if len(filtered_el_els) > 0:
            r += '        self.ignore_sub_elements.extend([\n'
            for el_el in filtered_el_els:
                r += '            \'{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}' + el_el.attrib['name'] + '\',\n'
            r += '        ])\n'

        el_attribs = el.findall('.//xsd:attribute', prefix_map)
        if len(el_attribs) > 0:
            r += '        self.ignore_attributes.extend([\n'
            for el_attrib in el_attribs:
                r += '            \'' + el_attrib.attrib['name'] + '\',\n'
            r += '        ])\n'
        print r

        print
        raw_input('Write? ')
        with open(sys.argv[2] + '/' + el.attrib['name'] + '.py', 'w') as cls_file:
            print >> cls_file, r
