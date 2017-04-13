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

from scap.model.xccdf_1_1.SelectableItemType import SelectableItemType
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class GroupType(SelectableItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'GroupIDPattern'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}Value': {'class': 'ValueType', 'map': 'items', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}Group': {'class': 'GroupType', 'map': 'items', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}Rule': {'class': 'RuleType', 'map': 'items', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': 1},
        },
    }

    def resolve(self, benchmark):
        ### Loading.Resolve.Items

        # For each Item in the Benchmark that has an extends property, resolve
        # it by using the following steps:
        if self.extends == '':
            return

        # (1) if the Item is Group, resolve all the enclosed Items,
        for item_id in self.items:
            self.items[item_id].resolve(benchmark)

        # (2) resolve the extended Item,
        # TODO

        # (3) prepend the property sequence from the extended Item to the
        # extending Item,
        # TODO

        # (4) if the Item is a Group, assign values for the id properties of
        # Items copied from the extended Group,
        # TODO

        # (5) remove duplicate properties and apply property overrides, and
        # TODO

        # (6) remove the extends property.
        # TODO

        # If any Item’s extends property identifier does not match the
        # identifier of a visible Item of the same type, then Loading fails.
        # TODO

        # If the directed graph formed by the extends properties includes a
        # loop, then Loading fails.
        # TODO

        # Otherwise, go to the next step: Loading.Resolve.Profiles.

        pass

    def process(self, benchmark):
        super(GroupType, self).process(benchmark)

        ### Group.Front

        # If the Item is a Group, then process the properties of the Group.
        # TODO

        ### Group.Content

        # If the Item is a Group, then for each Item in the Group’s items
        # property, initiate Item.Process.
        # TODO
