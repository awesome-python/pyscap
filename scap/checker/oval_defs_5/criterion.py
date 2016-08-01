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
class criterion(Checker):
    def __init__(self, host, content, args=None):
        super(criterion, self).__init__(host, content, args)

        test = content.resolve()
        try:
            self.checker = Checker.load(host, test, args)
        except ImportError:
            raise NotImplementedError('Test type ' + test.model_namespace + '.' \
                + test.__class__.__name__ + ' has not been implemented')

    def check(self):
        # TODO applicability_check?
        result = self.checker.check()

        from scap.model.oval_defs_5.Operators import Operators
        if self.content.negate:
            return Operators.negate(result)
        else:
            return result