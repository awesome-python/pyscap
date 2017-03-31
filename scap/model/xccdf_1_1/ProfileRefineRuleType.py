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
