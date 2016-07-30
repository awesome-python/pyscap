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
class criteria(Checker):
    def __init__(self, host, content, args=None):
        super(criteria, self).__init__(host, content, args)

        self.checkers = []
        for crit in content.criteria:
            self.checkers.append(Checker.load(host, crit, args))

    def check(self):
        # TODO operator, negate
        # TODO applicability_check?
        for checker in self.checkers:
            return checker.check()
