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

from scap.model.xccdf_1_2.ItemType import ItemType
import logging

logger = logging.getLogger(__name__)
class SelectableItemType(ItemType):
    ATTRIBUTE_MAP = {
        'selected': {'type': 'Boolean', 'default': True},
        'weight': {'type': 'Weight', 'default': 1.0},
    }
    TAG_MAP = {
        '{http://checklists.nist.gov/xccdf/1.2}rationale': {'ignore': True, 'class': 'HTMLTextWithSubType'},
        '{http://checklists.nist.gov/xccdf/1.2}platform': {'ignore': True, 'class': 'OverrideableCPE2IDRefType'},
        '{http://checklists.nist.gov/xccdf/1.2}requires': {'ignore': True, 'class': 'IDRefListType'},
        '{http://checklists.nist.gov/xccdf/1.2}conflicts': {'ignore': True, 'class': 'IDRefType'},
    }
    # abstract
