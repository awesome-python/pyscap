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
class Value(Simple):
    def __init__(self):
        super(Value, self).__init__()

        self.value = None

        self.tag_name = '{http://oval.mitre.org/XMLSchema/oval-definitions-5}value'

    def from_xml(self, paren, sub_el):
        super(Value, self).from_xml(parent, sub_el)

        self.value = sub_el.text
