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

from scap.model.xs.NormalizedString import NormalizedString
import logging

logger = logging.getLogger(__name__)
class ChoiceType(NormalizedString):
    def __init__(self):
        super(ChoiceType, self).__init__()

        self.var_ref = None

        # self.ignore_attributes.extend([
        # ])
        # self.ignore_sub_elements.extend([
        # ])

    def parse_attribute(self, name, value):
        if name == 'var_ref':
            self.var_ref = value
        else:
            return super(ChoiceType, self).parse_attribute(name, value)
        return True
