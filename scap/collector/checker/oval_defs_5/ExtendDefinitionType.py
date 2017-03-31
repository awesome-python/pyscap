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
class ExtendDefinitionType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(ExtendDefinitionType, self).__init__(host, content, parent, args)

        self.checker = Checker.load(host, self.resolve_reference(content.definition_ref), self, args)

    def collect(self):
        # TODO applicability_check?

        result = self.checker.collect()
        from scap.model.oval_common_5 import OperatorEnumeration
        if self.content.negate:
            return OperatorEnumeration.negate(result)
        else:
            return result
