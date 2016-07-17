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

from scap.model.content import Content
import logging
from scap.engine.engine import Engine

logger = logging.getLogger(__name__)
class Criteria(Content):
    def __init__(self, parent, el):
        super(self.__class__, self).__init__(parent, el)

        if 'operator' in el.attrib:
            self.operator = el.attrib['operator']
        else:
            self.operator = 'AND'

        if 'negate' in el.attrib and (el.attrib['negate'] == 'true' or el.attrib['negate'] == '1'):
            self.negate = True
        else:
            self.negate = False

        if 'applicability_check' in el.attrib and (el.attrib['applicability_check'] == 'true' or el.attrib['applicability_check'] == '1'):
            self.applicability_check = True
        else:
            self.applicability_check = False

        from scap.model.oval_defs_5.criterion import Criterion
        from scap.model.oval_defs_5.extend_definition import ExtendDefinition
        self.criteria = []
        for crit_el in el:
            if crit_el.tag.endswith('criteria'):
                self.criteria.append(Criteria(self, crit_el))
            elif crit_el.tag.endswith('criterion'):
                self.criteria.append(Criterion(self, crit_el))
            elif crit_el.tag.endswith('extend_definition'):
                self.criteria.append(ExtendDefinition(self, crit_el))
            else:
                logger.critical('Unknown tag in criteria: ' + crit_el.tag)
                import sys
                sys.exit()
