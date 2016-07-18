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
from scap.engine.engine import Engine

logger = logging.getLogger(__name__)
class LocalVariable(Variable):
    def __init__(self, parent, el):
        super(self.__class__, self).__init__(parent, el)

        from scap.model.oval_defs_5.component.object_component import ObjectComponent
        from scap.model.oval_defs_5.component.variable_component import VariableComponent
        from scap.model.oval_defs_5.component.literal_component import LiteralComponent
        from scap.model.oval_defs_5.component.functions_group import FunctionsGroup
        self.components = []
        for comp_el in el:
            if comp_el.tag.endswith('object_component'):
                self.components.append(ObjectComponent(self, comp_el))
            elif comp_el.tag.endswith('variable_component'):
                self.components.append(VariableComponent(self, comp_el))
            elif comp_el.tag.endswith('literal_component'):
                self.components.append(LiteralComponent(self, comp_el))
            elif comp_el.tag.endswith('functions'):
                self.components.append(FunctionsGroup(self, comp_el))
            else:
                logger.critical('Unknown component in variable ' + self.id)
                import sys
                sys.exit()
