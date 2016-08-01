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
class check(Checker):
    def __init__(self, host, content, args=None):
        super(check, self).__init__(host, content, args)

        self.checkers = []
        content = self.content.resolve()
        if isinstance(content, list):
            for defn in content:
                self.checkers.append(Checker.load(host, defn, args))
        else:
            self.checkers.append(Checker.load(host, content, args))

    def check(self):
        # TODO: multi-check

        from scap.model.xccdf_1_2.Operators import Operators
        results = []
        for checker in self.checkers:
            if checker.content.model_namespace.startswith('oval'):
                results.append(Operators.oval_translate(checker.check()))
            else:
                raise NotImplementedError('Unknown model namespace: ' + checker.content.model_namespace)

        result = Operators.AND(results)

        if self.content.negate:
            return Operators.negate(result)
        else:
            return result
