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

from scap.model.ocil_2_0.TestActionCondition import TestActionCondition
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class when_range(TestActionCondition):
    def __init__(self):
        super(when_range, self).__init__()

        self.ranges = []

        # self.ignore_attributes.extend([
        # ])
        # self.ignore_sub_elements.extend([
        # ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}range':
            self.ranges.append(Model.load_child(self, sub_el))
        else:
            return super(when_range, self).parse_sub_el(sub_el)
        return True
