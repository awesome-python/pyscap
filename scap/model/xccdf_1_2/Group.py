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

from scap.model.xccdf_1_2.SelectableItem import SelectableItem
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class Group(SelectableItem):
    def __init__(self):
        super(Group, self).__init__()
        self.values = {}
        self.rules = {}
        self.groups = {}

        self.required_attributes.append('id')
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Value':
            self.values[sub_el.attrib['id']] = Model.load(self, sub_el)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Group':
            g = Model.load(self, sub_el)
            self.groups[sub_el.attrib['id']] = g
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Rule':
            r = Model.load(self, sub_el)
            self.rules[sub_el.attrib['id']] = r
        else:
            return super(Group, self).parse_sub_el(sub_el)
        return True

    def get_values(self):
        values = self.values.copy()
        for g in self.groups.values():
            values.update(g.get_values())
        return values

    def get_rules(self):
        rules = self.rules.copy()
        for g in self.groups.values():
            rules.update(g.get_rules())
        return rules
