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

from scap.model.oval_defs_5.variable import Variable
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class ConstantVariable(Variable):
    def from_xml(self, parent, el):
        super(ConstantVariable, self).from_xml(parent, el)

        self.values = []
        for v_el in el.findall('./oval_defs_5:value'):
            if 'value' not in v_el.attrib:
                logger.critical('value element missing value attribute')
                import sys
                sys.exit()
            self.values.append(v_el.attrib['value'])
