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

from scap.model.xs.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class PossibleValueType(Simple):
    def __init__(self):
        super(PossibleValueType, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}possible_value

        self.hint = None

    def parse_attribute(self, name, value):
        if name == 'hint':
            self.hint = value
        else:
            return super(PossibleValueType, self).parse_attribute(name, value)
        return True
