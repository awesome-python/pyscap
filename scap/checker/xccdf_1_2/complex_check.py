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

from scap.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class complex_check(Checker):
    def __init__(self, host, content, args=None):
        super(complex_check, self).__init__(host, content, args)

        self.checkers = []
        for check in content.checks:
            self.checkers.append(Checker.load(host, check, args))

    def check(self):
        from scap.model.xccdf_1_2.Operators import Operators
        result = self.checkers[0].check()
        for i in range(1, len(self.checkers)):
            if self.content.operator == 'AND':
                result = Operators.AND(result, self.checkers[i].check())
            elif self.content.operator == 'OR':
                result = Operators.OR(result, self.checkers[i].check())
            else:
                raise NotImplementedError('Unknown complex_check operator: ' + self.content.operator)

        if self.content.negate:
            return Operators.negate(result)
        else:
            return result
