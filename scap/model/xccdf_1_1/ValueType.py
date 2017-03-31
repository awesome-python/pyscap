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

from scap.model.xccdf_1_1.ItemType import ItemType
from scap.model.xccdf_1_1.ValueTypeEnumeration import VALUE_TYPE_ENUMERATION
from scap.model.xccdf_1_1.ValueOperatorEnumeration import VALUE_OPERATOR_ENUMERATION
from scap.model.xccdf_1_1.InterfaceHintEnumeration import INTERFACE_HINT_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class ValueType(ItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'type': 'ValueIDPattern', 'required': True},
            'type': {'enum': VALUE_TYPE_ENUMERATION, 'default': 'string'},
            'operator': {'enum': VALUE_OPERATOR_ENUMERATION, 'default': 'equals'},
            'interactive': {'ignore': True, 'type': 'Boolean'},
            'interfaceHint': {'ignore': True, 'enum': INTERFACE_HINT_ENUMERATION},
        },
        'elements': {
            # TODO: at least one value
            # TODO: since order matters in xml (and for values) we might need a list vs. dict here
            '{http://checklists.nist.gov/xccdf/1.1}value': {'class': 'SelStringType', 'map': 'values', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}complex-value': {'class': 'SelComplexValueType', 'map': 'complex_values', 'key': 'selector', 'min': 0, 'max': None},
            # choice of below
            '{http://checklists.nist.gov/xccdf/1.1}default': {'class': 'SelStringType', 'min': 0, 'max': None, 'map': 'defaults', 'key': 'selector'},
            '{http://checklists.nist.gov/xccdf/1.1}complex-default': {'class': 'SelComplexValueType', 'min': 0, 'max': None, 'map': 'complex_defaults', 'key': 'selector'},

            '{http://checklists.nist.gov/xccdf/1.1}match': {'class': 'SelStringType', 'map': 'matches', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}lower-bound': {'class': 'SelNumType', 'map': 'lower_bounds', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}upper-bound': {'class': 'SelNumType', 'map': 'upper_bounds', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}choices': {'class': 'SelChoicesType', 'map': 'choices', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}source': {'class': 'URIRefType', 'append': 'sources', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': None},
        },
    }
