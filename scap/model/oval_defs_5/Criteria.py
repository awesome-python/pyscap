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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class Criteria(Simple):
    def __init__(self):
        super(Criteria, self).__init__()

        self.operator = 'AND'
        self.negate = False
        self.applicability_check = False
        self.criteria = []

        self.tag_name = '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria'
        # self.ignore_attributes.extend([
        # ])

    def parse_attribute(self, name, value):
        if name == 'operator':
            self.operator = value
        elif name == 'negate':
            self.negate = self.parse_boolean(value)
        elif name == 'applicability_check':
            self.applicability_check = self.parse_boolean(value)
        else:
            return super(Criteria, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        from scap.model.oval_defs_5.Criterion import Criterion
        from scap.model.oval_defs_5.ExtendDefinition import ExtendDefinition
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria':
            c = Criteria()
            c.from_xml(self, sub_el)
            self.criteria.append(c)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criterion':
            c = Criterion()
            c.from_xml(self, sub_el)
            self.criteria.append(c)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}extend_definition':
            ed = ExtendDefinition()
            ed.from_xml(self, sub_el)
            self.criteria.append(ed)
        else:
            return super(Criteria, self).parse_sub_el(sub_el)
        return True
