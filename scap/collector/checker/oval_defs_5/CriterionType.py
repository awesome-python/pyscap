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
class CriterionType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(CriterionType, self).__init__(host, content, parent, args)

        test = self.resolve_reference(content.test_ref)
        try:
            self.checker = Checker.load(host, test, self, args)
        except ImportError:
            raise NotImplementedError('Test checker type scap.collector.checker.' + test.model_namespace + '.' \
                + test.__class__.__name__ + ' has not been implemented')

    def collect(self):
        # TODO applicability_check?
        result = self.checker.collect()

        from scap.model.oval_common_5 import OperatorEnumeration
        if self.content.negate:
            return OperatorEnumeration.negate(result)
        else:
            return result
