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

from scap.model.oval_defs_5.component.function import Function
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Count(Function):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        self.values = []
        for comp_el in el:
            self.values.append(Component.load(self, comp_el))
        if len(self.values) < 1:
            logger.critical('CountFunction with len(values) < 1')
            import sys
            sys.exit()
