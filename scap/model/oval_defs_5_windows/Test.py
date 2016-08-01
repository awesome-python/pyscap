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

import scap.model.oval_defs_5.Test
import logging

logger = logging.getLogger(__name__)

class Test(scap.model.oval_defs_5.Test.Test):
    def __init__(self):
        super(Test, self).__init__()

        self.object_ref = None
        self.state_refs = []

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}object':
            self.object_ref = sub_el.attrib['object_ref']
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}state':
            self.state_refs.append(sub_el.attrib['state_ref'])
        else:
            return super(Test, self).parse_sub_el(sub_el)
        return True

    def resolve_object(self):
        if self.object_ref is None:
            return None
        return self.resolve_reference(self.object_ref)

    def resolve_states(self):
        states = []
        for ref in self.state_refs:
            states.append(self.resolve_reference(ref))
        return states
