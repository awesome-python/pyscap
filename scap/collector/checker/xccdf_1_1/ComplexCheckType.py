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

from scap.collector.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class ComplexCheckType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(ComplexCheckType, self).__init__(host, content, parent, args)

        self.checkers = []
        for check in content.checks:
            self.checkers.append(Checker.load(host, check, self, args))

    def collect(self):
        from scap.model.xccdf_1_1 import CheckOperatorEnumeration
        results = []
        for checker in self.checkers:
            if checker.content.model_namespace.startswith('oval'):
                results.append(CheckOperatorEnumeration.oval_translate(checker.collect()))
            else:
                raise NotImplementedError('Unknown model namespace: ' + checker.content.model_namespace)

        if self.content.operator == 'AND':
            result = CheckOperatorEnumeration.AND(results)
        elif self.content.operator == 'OR':
            result = CheckOperatorEnumeration.OR(results)
        else:
            raise NotImplementedError('Unknown complex_check operator: ' + self.content.operator)

        if self.content.negate:
            return CheckOperatorEnumeration.negate(result)
        else:
            return result
