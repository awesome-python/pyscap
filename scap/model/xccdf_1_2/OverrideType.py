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

from scap.model.xs.Decimal import Decimal
from scap.model.xccdf_1_2.ResultEnumeration import RESULT_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class OverrideType(Decimal):
    MODEL_MAP = {
        'attributes': {
            'time': {'type': 'DateTime', 'required': True},
            'authority': {'type': 'String', 'required': True},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}old-result': {'enum': RESULT_ENUMERATION},
            '{http://checklists.nist.gov/xccdf/1.2}new-result': {'enum': RESULT_ENUMERATION},
            '{http://checklists.nist.gov/xccdf/1.2}remark': {'class': 'TextType'},
        },
    }
