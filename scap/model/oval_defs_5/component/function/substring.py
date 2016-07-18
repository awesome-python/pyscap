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

from scap.model.oval_defs_5.component.function.function import Function
import logging
from scap.engine.engine import Engine

logger = logging.getLogger(__name__)
class SubstringFunction(Function):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        if 'substring_start' not in el.attrib:
            logger.critical('SubstringFunction does not define substring_start')
            import sys
            sys.exit()
        self.substring_start = el.attrib['substring_start']

        if 'substring_length' not in el.attrib:
            logger.critical('SubstringFunction does not define substring_length')
            import sys
            sys.exit()
        self.substring_length = el.attrib['substring_length']

        self.values = []
        for comp_el in el:
            self.values.append(Component.load(self, comp_el))
        if len(self.values) != 1:
            logger.critical('SubstringFunction with != len(values)')
            import sys
            sys.exit()
