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

from scap.model.xccdf_1_2.SelectableItemType import SelectableItemType
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class GroupType(SelectableItemType):
    ATTRIBUTE_MAP = {
        'id': {'required': True, 'type': 'GroupIDPattern'},
    }
    TAG_MAP = {
        '{http://checklists.nist.gov/xccdf/1.2}Value': {'class': 'ValueType', 'map': 'values'},
        '{http://checklists.nist.gov/xccdf/1.2}Group': {'class': 'GroupType', 'map': 'groups'},
        '{http://checklists.nist.gov/xccdf/1.2}Rule': {'class': 'RuleType', 'map': 'rules'},
        '{http://checklists.nist.gov/xccdf/1.2}signature': {'ignore': True, 'class': 'SignatureType'},
    }

    # def __init__(self):
    #     super(GroupType, self).__init__()
    #     self.values = {}
    #     self.rules = {}
    #     self.groups = {}
