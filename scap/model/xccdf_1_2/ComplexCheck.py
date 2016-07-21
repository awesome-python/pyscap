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
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class ComplexCheck(Simple):
    def __init__(self):
        super(ComplexCheck, self).__init__()
        self.checks = []
        self.negate = False
        self.operator = 'AND'

    def parse_attrib(self, name, value):
        ignore = []
        if name in ignore:
            return True
        elif name == 'negate':
            self.negate = self.parse_boolean(value)
        elif name == 'operator':
            self.negate = value
        else:
            return super(Rule, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        ignore = []
        if sub_el.tag in ignore:
            return True
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}complex-check':
            check = ComplexCheck()
            check.from_xml(self, sub_el)
            self.checks.append(check)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}check':
            from scap.model.xccdf_1_2.Check import Check
            check = Check()
            check.from_xml(self, sub_el)
            self.checks.append(check)
        else:
            return super(Rule, self).parse_sub_el(sub_el)
        return True
