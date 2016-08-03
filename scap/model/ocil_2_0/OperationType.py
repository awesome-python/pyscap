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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class OperationType(Model):
    TAG_MAP = {
        '{http://scap.nist.gov/schema/ocil/2.0}test_action_ref': {'class': 'TestActionRefType'},
        '{http://scap.nist.gov/schema/ocil/2.0}actions': {'class': 'OperationType'},
    }
    def __init__(self):
        super(OperationType, self).__init__()

        self.operation = 'AND'
        self.negate = False

        self.test_action_refs = []

    def parse_attribute(self, name, value):
        if name == 'operation':
            self.operation = value
        elif name == 'negate':
            self.negate = self.parse_boolean(value)
        else:
            return super(OperationType, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}test_action_ref':
            for sub_sub_el in sub_el:
                self.test_action_refs.append(Model.load(self, sub_sub_el))
        else:
            return super(OperationType, self).parse_sub_el(sub_el)
        return True
