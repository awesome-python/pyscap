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

from scap.model.xccdf_1_2.Item import Item
import logging

logger = logging.getLogger(__name__)
class SelectableItem(Item):
    def __init__(self):
        super(SelectableItem, self).__init__()

        self.selected = True
        self.weight = 1.0

        self.ignore_attributes.extend([
            'selected',
            'weight',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}rationale',
            '{http://checklists.nist.gov/xccdf/1.2}platform',
            '{http://checklists.nist.gov/xccdf/1.2}requires',
            '{http://checklists.nist.gov/xccdf/1.2}conflicts',
        ])

    def parse_attribute(self, name, value):
        if name == 'selected':
            self.selected = self.parse_boolean(value)
        elif name == 'weight':
            self.weight = value
        else:
            return super(SelectableItem, self).parse_attribute(name, value)
        return True
