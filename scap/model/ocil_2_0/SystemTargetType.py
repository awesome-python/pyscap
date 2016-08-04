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

from scap.model.ocil_2_0.TargetType import TargetType
import logging

logger = logging.getLogger(__name__)
class SystemTargetType(TargetType):
    def __init__(self):
        super(SystemTargetType, self).__init__()

        self.organization = None
        self.ipaddress = None
        self.description = None

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}organization':
            self.organization = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}ipaddress':
            self.ipaddress = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}description':
            self.description = sub_el.text
        else:
            return super(SystemTargetType, self).parse_element(sub_el)
        return True
