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
class Function(Model):
    def __init__(self):
        super(Function, self).__init__()

        self.components = []

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}object_component':
            from scap.model.oval_defs_5.ObjectComponent import ObjectComponent
            comp = ObjectComponent()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variable_component':
            from scap.model.oval_defs_5.VariableComponent import VariableComponent
            comp = VariableComponent()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}literal_component':
            from scap.model.oval_defs_5.LiteralComponent import LiteralComponent
            comp = LiteralComponent()

        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}arithmetic':
            from scap.model.oval_defs_5.Arithmetic import Arithmetic
            comp = Arithmetic()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}begin':
            from scap.model.oval_defs_5.Begin import Begin
            comp = Begin()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}concat':
            from scap.model.oval_defs_5.Concat import Concat
            comp = Concat()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}count':
            from scap.model.oval_defs_5.Count import Count
            comp = Count()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}end':
            from scap.model.oval_defs_5.End import End
            comp = End()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}escape_regex':
            from scap.model.oval_defs_5.EscapeRegex import EscapeRegex
            comp = EscapeRegex()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}split':
            from scap.model.oval_defs_5.Split import Split
            comp = Split()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}substring':
            from scap.model.oval_defs_5.Substring import Substring
            comp = Substring()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}time_difference':
            from scap.model.oval_defs_5.TimeDifference import TimeDifference
            comp = TimeDifference()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}unique':
            from scap.model.oval_defs_5.Unique import Unique
            comp = Unique()
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}regex_capture':
            from scap.model.oval_defs_5.RegexCapture import RegexCapture
            comp = RegexCapture()
        else:
            return super(Function, self).parse_sub_el(sub_el)
        comp.from_xml(self, sub_el)
        self.components.append(comp)
        return True
