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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class criteria(Model):
    def __init__(self):
        super(criteria, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria

        self.operator = 'AND'
        self.negate = False
        self.applicability_check = False
        self.criteria = []

    def parse_attribute(self, name, value):
        if name == 'operator':
            self.operator = value
        elif name == 'negate':
            self.negate = self.parse_boolean(value)
        elif name == 'applicability_check':
            self.applicability_check = self.parse_boolean(value)
        else:
            return super(criteria, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria' \
            or sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criterion' \
            or sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}extend_definition':
            self.criteria.append(Model.load(self, sub_el))
        else:
            return super(criteria, self).parse_sub_el(sub_el)
        return True
