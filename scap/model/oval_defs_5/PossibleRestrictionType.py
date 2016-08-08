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
class PossibleRestrictionType(Model):
    'elements': {
        '{http://oval.mitre.org/XMLSchema/oval-definitions-5}restriction': {'class': 'RestrictionType'},
    }
    def __init__(self):
        super(PossibleRestrictionType, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}possible_restriction

        self.hint = None
        self.operator = 'AND'
        self.children = []

    def parse_attribute(self, name, value):
        if name == 'hint':
            self.hint = value
        elif name == 'operator':
            self.operator = value
        else:
            return super(PossibleRestrictionType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}restriction':
            self.children.append(Model.load(self, sub_el))
        else:
            return super(PossibleRestrictionType, self).parse_element(sub_el)
        return True
