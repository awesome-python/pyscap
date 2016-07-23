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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class Set(Simple):
    def __init__(self):
        super(Set, self).__init__()

        self.set_operator = 'UNION'
        self.children = []

        self.tag_name = '{http://oval.mitre.org/XMLSchema/oval-definitions-5}set'

    def parse_attribute(self, name, value):
        if name == 'set_operator':
            self.set_operator = value
        else:
            return super(Set, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}set':
            s = Set()
            s.from_xml(self, sub_el)
            self.children.append(s)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}object_reference':
            o = ObjectReference()
            o.from_xml(self, sub_el)
            self.children.append(o)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}filter':
            fail = Filter()
            f.from_xml(self, sub_el)
            self.children.append(f)
        else:
            return super(OVALDefinitions, self).parse_sub_el(sub_el)
        return True
