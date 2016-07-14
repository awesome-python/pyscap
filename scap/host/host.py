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

import inspect

class Host(object):
    def discover_hardware(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented for class: ' + self.__class__.__name__)
    def discover_software(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented for class: ' + self.__class__.__name__)
    def test_rule(self, rule, values, content):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented for class: ' + self.__class__.__name__)
    def get_arf_1_1(self):
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented for class: ' + self.__class__.__name__)
