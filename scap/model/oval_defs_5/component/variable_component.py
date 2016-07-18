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

from scap.model.oval_defs_5.component.component import Component
import logging
from scap.engine.engine import Engine

logger = logging.getLogger(__name__)
class VariableComponent(Component):
    def __init__(self, parent, el):
        super(self.__class__, self).__init__(parent, el)

        if 'var_ref' not in el.attrib:
            logger.critical('variable component missing var_ref attribute')
            import sys
            sys.exit()
        self.var_ref = el.attrib['var_ref']
