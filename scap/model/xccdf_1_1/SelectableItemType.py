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
import logging

logger = logging.getLogger(__name__)
class SelectableItemType(ItemType):
    MODEL_MAP = {
        'attributes': {
            'selected': {'type': 'Boolean', 'default': True},
            'weight': {'type': 'Weight', 'default': 1.0},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}rationale': {'append': 'rationales', 'ignore': True, 'min': 0, 'max': None, 'class': 'HTMLTextWithSubType'},
            '{http://checklists.nist.gov/xccdf/1.1}platform': {'append': 'platforms', 'ignore': True, 'min': 0, 'max': None, 'class': 'OverrideableCPE2IDRefType'},
            '{http://checklists.nist.gov/xccdf/1.1}requires': {'append': 'requires', 'ignore': True, 'min': 0, 'max': None, 'class': 'IDRefListType'},
            '{http://checklists.nist.gov/xccdf/1.1}conflicts': {'append': 'conflicts', 'ignore': True, 'min': 0, 'max': None, 'class': 'IDRefType'},
        },
    }
    # abstract
