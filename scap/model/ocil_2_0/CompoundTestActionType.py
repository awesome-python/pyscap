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

from scap.model.ocil_2_0.TestActionType import TestActionType
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class CompoundTestActionType(TestActionType):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}reference': {'class': 'ReferenceType'},
            '{http://scap.nist.gov/schema/ocil/2.0}actions': {'class': 'OperationType'},
        }
    }
    def __init__(self):
        super(CompoundTestActionType, self).__init__()

        self.title = None
        self.description = None
        self.references = []
        self.actions = None

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}title':
            self.title = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}description':
            self.description = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}references':
            for sub_sub_el in sub_el:
                self.references.append(Model.load(self, sub_sub_el))
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}actions':
            self.actions = Model.load(self, sub_el)
        else:
            return super(CompoundTestActionType, self).parse_element(sub_el)
        return True
