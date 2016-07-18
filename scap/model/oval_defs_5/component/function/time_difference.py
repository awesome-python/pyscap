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
class TimeDifferenceFunction(Function):
    def __init__(self, parent, el):
        super(self.__class__, self).__init__(parent, el)

        if 'format_1' in el.attrib:
            self.format_1 = el.attrib['format_1']
        else:
            self.format_1 = 'year_month_day'

        if 'format_2' in el.attrib:
            self.format_2 = el.attrib['format_2']
        else:
            self.format_2 = 'year_month_day'

        self.values = []
        for comp_el in el:
            self.values.append(Component.load(self, comp_el))
        if len(self.values) < 1 or len(self.values) > 2:
            logger.critical('TimeDifferenceFunction with len(values) < 1 or len(values) > 2')
            import sys
            sys.exit()
