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

from scap.Model import Model
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class OVALDefinitions(Model):
    def from_xml(self, parent, el):
        super(OVALDefinitions, self).from_xml(parent, el)

        from scap.model.oval_defs_5.Definition import Definition
        self.definitions = {}
        for def_el in el.findall('./oval_defs_5:definitions/oval_defs_5:definition', Engine.namespaces):
            d = Definition()
            d.from_xml(self, def_el)
            self.definitions[def_el.attrib['id']] = d

        from scap.model.oval_defs_5.Test import Test
        self.tests = {}
        for test_el in el.findall('./oval_defs_5:tests/oval_defs_5:test', Engine.namespaces):
            t = Test()
            t.from_xml(self, test_el)
            self.definitions[test_el.attrib['id']] = t

        from scap.model.oval_defs_5.Object import Object
        self.objects = {}
        for obj_el in el.findall('./oval_defs_5:objects/oval_defs_5:object', Engine.namespaces):
            o = Object()
            o.from_xml(self, obj_el)
            self.objects[obj_el.attrib['id']] = o

        from scap.model.oval_defs_5.State import State
        self.states = {}
        for state_el in el.findall('./oval_defs_5:states/oval_defs_5:state', Engine.namespaces):
            s = State()
            s.from_xml(self, state_el)
            self.states[state_el.attrib['id']] = s

        from scap.model.oval_defs_5.Variable import Variable
        self.variables = {}
        for var_el in el.findall('./oval_defs_5:variables/oval_defs_5:variable', Engine.namespaces):
            v = Variable()
            v.from_xml(self, var_el)
            self.variables[var_el.attrib['id']] = v
