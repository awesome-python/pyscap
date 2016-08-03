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

from scap.model.xccdf_1_2.ItemType import ItemType
import logging

logger = logging.getLogger(__name__)
class ValueType(ItemType):
    def __init__(self):
        super(ValueType, self).__init__()
        self.selectors = {}
        self.type = 'string'
        self.operator = 'equals'

        self.ignore_attributes.extend([
            'interactive',
            'interfaceHint',
        ])

        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}complex-value',
            '{http://checklists.nist.gov/xccdf/1.2}default',
            '{http://checklists.nist.gov/xccdf/1.2}complex-default',
            '{http://checklists.nist.gov/xccdf/1.2}match',
            '{http://checklists.nist.gov/xccdf/1.2}lower-bound',
            '{http://checklists.nist.gov/xccdf/1.2}upper-bound',
            '{http://checklists.nist.gov/xccdf/1.2}choices',
            '{http://checklists.nist.gov/xccdf/1.2}source',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_attribute(self, name, value):
        if name == 'type':
            self.type = value
        elif name == 'operator':
            self.operator = value
        else:
            return super(ValueType, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}value':
            if 'selector' in sub_el.attrib:
                logger.debug('Selector value of ' + self.id + ' ' + sub_el.attrib['selector'] + ' = ' + str(sub_el.text))
                if sub_el.text is None:
                    self.selectors[sub_el.attrib['selector']] = ''
                else:
                    self.selectors[sub_el.attrib['selector']] = sub_el.text
            else:
                logger.debug('Default value of ' + self.id + ' is ' + str(sub_el.text))
                if sub_el.text is None:
                    self.selectors[None] = ''
                else:
                    self.selectors[None] = sub_el.text
        else:
            return super(ValueType, self).parse_sub_el(sub_el)
        return True
