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

from scap.model.xccdf_1_2.Item import Item
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Value(Item):
    def __init__(self):
        super(Value, self).__init__()
        self.selectors = {}
        self.default = None

    def parse_attrib(self, name, value):
        ignore = [
        ]
        if name in ignore:
            return True
        elif name == 'type':
            self.type = value
        elif name == 'operator':
            self.operator = value
        else:
            return super(Value, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        ignore = [
        ]
        if sub_el.tag in ignore:
            return True
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}value':
            if 'selector' in sub_el.attrib:
                logger.debug('Selector value of ' + self.id + ' ' + sub_el.attrib['selector'] + ' = ' + str(sub_el.text))
                self.selectors[sub_el.attrib['selector']] = sub_el.text
            else:
                logger.debug('Default value of ' + self.id + ' is ' + str(sub_el.text))
                self.default = sub_el.text
        else:
            return super(Value, self).parse_sub_el(sub_el)
        return True
