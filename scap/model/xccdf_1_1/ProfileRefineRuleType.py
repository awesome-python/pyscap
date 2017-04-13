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

from scap.Model import Model
from scap.model.xccdf_1_1.SeverityEnumeration import SEVERITY_ENUMERATION
from scap.model.xccdf_1_1.RoleEnumeration import ROLE_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class ProfileRefineRuleType(Model):
    MODEL_MAP = {
        'attributes': {
            'idref': {'type': 'NCName', 'required': True},
            'weight': {'type': 'Weight'},
            'selector': {'type': 'String'},
            'severity': {'enum': SEVERITY_ENUMERATION},
            'role': {'enum': ROLE_ENUMERATION},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}remark': {'ignore': True, 'type': 'TextType', 'append': 'remarks', 'min': 0, 'max': None},
        },
    }

    def apply(self, item):
        from scap.model.xccdf_1_1.RuleType import RuleType
        if not isinstance(item, RuleType):
            raise ValueError('Trying to refine rule (' + self.idref + ') on an item of the wrong type: ' + item.__class__.__name__)

        if self.weight is not None:
            logger.debug('Refining rule ' + item.id + ' weight to ' + self.weight)
            item.weight = float(self.weight)

        if self.selector is not None:
            logger.debug('Refining rule ' + item.id + ' check to ' + self.selector)
            item.check_selector = self.selector

        if self.severity is not None:
            logger.debug('Refining rule ' + item.id + ' severity to ' + self.severity)
            item.severity = self.severity

        if self.role is not None:
            logger.debug('Refining rule ' + item.id + ' role to ' + self.role)
            item.role = self.role
