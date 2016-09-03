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
from scap.model.oval_common_5.OperatorEnumeration import OPERATOR_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class CriteriaType(Model):
    MODEL_MAP = {
        'elements': {
            # TODO minOccurs="1" maxOccurs="unbounded" of the following:
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria': {'append': 'criteria', 'class': 'CriteriaType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criterion': {'append': 'criteria', 'class': 'CriterionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}extend_definition': {'append': 'criteria', 'class': 'ExtendDefinitionType'},
        },
        'attributes': {
            'applicability_check': {'type': 'Boolean'},
            'operator': {'enum': OPERATOR_ENUMERATION, 'default': 'AND'},
            'negate': {'type': 'Boolean', 'default': False},
            'comment': {'type': 'oval_common_5.NonEmptyString'},
        }
    }
