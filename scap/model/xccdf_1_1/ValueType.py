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
            '{http://checklists.nist.gov/xccdf/1.1}default': {'class': 'SelStringType', 'min': 0, 'max': None, 'map': 'defaults', 'key': 'selector'},
            '{http://checklists.nist.gov/xccdf/1.1}match': {'class': 'SelStringType', 'map': 'matches', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}lower-bound': {'class': 'SelNumType', 'map': 'lower_bounds', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}upper-bound': {'class': 'SelNumType', 'map': 'upper_bounds', 'key': 'selector', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}choices': {'class': 'SelChoicesType', 'map': 'choice_selections', 'key': 'selector', 'min': 0, 'max': None},

            '{http://checklists.nist.gov/xccdf/1.1}source': {'class': 'URIRefType', 'append': 'sources', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': None},
        },
    }

    def __init__(self):
        super(ValueType, self).__init__()

        self.default = None
        self.value = None
        self.match = None
        self.lower_bound = None
        self.upper_bound = None
        self.choices = None

        self.default_selector = None
        self.value_selector = None
        self.match_selector = None
        self.lower_bound_selector = None
        self.upper_bound_selector = None
        self.choices_selector = None

    def process(self, benchmark, host):
        ### Value.Content

        # If the Item is a Value, then process the properties of the Value.

        # default
        if self.default_selector is not None and self.default_selector in self.defaults:
            self.default = self.defaults[self.default_selector]
        elif '' in self.defaults:
            self.default = self.defaults['']

        # value
        if self.value_selector is not None and self.value_selector in self.values:
            self.value = self.values[self.value_selector]
        elif self.default is not None:
            self.value = self.default
        elif '' in self.values:
            self.value = self.values['']

        # match
        if self.match_selector is not None and self.match_selector in self.matches:
            self.match = self.matches[self.match_selector]
        elif '' in self.matches:
            self.match = self.matches['']

        # lower_bound
        if self.lower_bound_selector is not None and self.lower_bound_selector in self.lower_bounds:
            self.lower_bound = self.lower_bounds[self.lower_bound_selector]
        elif '' in self.lower_bounds:
            self.lower_bound = self.lower_bounds['']

        # upper_bound
        if self.upper_bound_selector is not None and self.upper_bound_selector in self.upper_bounds:
            self.upper_bound = self.upper_bounds[self.upper_bound_selector]
        elif '' in self.upper_bounds:
            self.upper_bound = self.upper_bounds['']

        # choices
        if self.choices_selector is not None and self.choices_selector in self.choice_selections:
            self.choices = self.choice_selections[self.choice_selector]
        elif '' in self.choice_selections:
            self.choices = self.choice_selections['']
