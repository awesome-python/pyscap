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

from scap.model.ocil_2_0.ItemBaseType import ItemBaseType
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class QuestionTestActionType(ItemBaseType):
    MODEL_MAP = {
        # abstract
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}title': {'class': 'TextType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}when_unknown': {'class': 'TestActionConditionType', 'min': 0},
            '{http://scap.nist.gov/schema/ocil/2.0}when_not_tested': {'class': 'TestActionConditionType', 'min': 0},
            '{http://scap.nist.gov/schema/ocil/2.0}when_not_applicable': {'class': 'TestActionConditionType', 'min': 0},
            '{http://scap.nist.gov/schema/ocil/2.0}when_error': {'class': 'TestActionConditionType', 'min': 0},
        },
        'attributes': {
            'question_ref': {'type': 'QuestionIDPattern', 'required': True}
            'id': {'type': 'QuestionTestActionIDPattern', 'required': True}
        }
    }
