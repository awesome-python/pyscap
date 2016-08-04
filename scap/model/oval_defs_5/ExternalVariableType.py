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

from scap.model.oval_defs_5.Variable import Variable
import logging

logger = logging.getLogger(__name__)
class ExternalVariableType(Variable):
    def __init__(self):
        super(ExternalVariableType, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}external_variable

        self.children = []

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}possible_value':
            pv = PossibleValue()
            pv.from_xml(self, sub_el)
            self.children.append(pv)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}possible_restriction':
            pr = PossibleRestriction()
            pr.from_xml(self, sub_el)
            self.children.append(pr)
        else:
            return super(ExternalVariableType, self).parse_element(sub_el)
        return True
