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
from scap.model.xccdf_1_2.ResultEnumeration import RESULT_ENUMERATION
from scap.model.xccdf_1_2.RoleEnumeration import ROLE_ENUMERATION
from scap.model.xccdf_1_2.SeverityEnumeration import SEVERITY_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class RuleResultType(Model):
    MODEL_MAP = {
        'attributes': {
            'idref': {'type': 'NCName', 'required': True},
            'role': {'enum': ROLE_ENUMERATION},
            'severity': {'enum': SEVERITY_ENUMERATION},
            'time': {'type': 'DateTime'},
            'version': {'type': 'String'},
            'weight': {'type': 'Weight'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}result': {'enum': RESULT_ENUMERATION},
            '{http://checklists.nist.gov/xccdf/1.2}override': {'class': 'OverrideType', 'append': 'overrides'},
            '{http://checklists.nist.gov/xccdf/1.2}ident': {'class': 'IdentType', 'append': 'idents'},
            '{http://checklists.nist.gov/xccdf/1.2}metadata': {'class': 'MetadataType', 'append': 'metadata'},
            '{http://checklists.nist.gov/xccdf/1.2}message': {'class': 'MessageType', 'append': 'messages'},
            '{http://checklists.nist.gov/xccdf/1.2}instance': {'class': 'InstanceResultType', 'append': 'instances'},
            '{http://checklists.nist.gov/xccdf/1.2}fix': {'class': 'FixType', 'append': 'fixes'},
            '{http://checklists.nist.gov/xccdf/1.2}check': {'class': 'CheckType', 'append': 'checks'},
            '{http://checklists.nist.gov/xccdf/1.2}complex-check': {'class': 'ComplexCheckType'},
        },
    }
