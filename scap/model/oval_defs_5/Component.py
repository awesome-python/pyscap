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

from scap.model.oval_defs_5.component.ObjectComponent import ObjectComponent
from scap.model.oval_defs_5.component.VariableComponent import VariableComponent
from scap.model.oval_defs_5.component.LiteralComponent import LiteralComponent
from scap.model.oval_defs_5.component.Functions import Functions

from scap.model.oval_defs_5.component.function.Arithmetic import Arithmetic
from scap.model.oval_defs_5.component.function.Begin import Begin
from scap.model.oval_defs_5.component.function.Concat import Concat
from scap.model.oval_defs_5.component.function.Count import Count
from scap.model.oval_defs_5.component.function.End import End
from scap.model.oval_defs_5.component.function.EscapeRegex import EscapeRegex
from scap.model.oval_defs_5.component.function.Split import Split
from scap.model.oval_defs_5.component.function.Substring import Substring
from scap.model.oval_defs_5.component.function.TimeDifference import TimeDifference
from scap.model.oval_defs_5.component.function.Unique import Unique
from scap.model.oval_defs_5.component.function.RegexCapture import RegexCapture

logger = logging.getLogger(__name__)
class Component(Model):
    comp_map = {
        'object_component': ObjectComponent,
        'variable_component': VariableComponent,
        'literal_component': LiteralComponent,
        'functions': Functions,

        'arithmetic': Arithmetic,
        'begin': Begin,
        'concat': Concat,
        'count': Count,
        'end': End,
        'escape_regex': EscapeRegex,
        'split': Split,
        'substring': Substring,
        'time_difference': TimeDifference,
        'unique': Unique,
        'regex_capture': RegexCapture,
    }

    @staticmethod
    def load(parent, comp_el):
        if not comp_el.tag.startswith('{' + Engine.namespaces['oval_defs_5'] + '}'):
            logger.critical('Unknown component tag namespace: ' + comp_el.tag)
            import sys
            sys.exit()
        tag = comp_el.tag[len('{' + Engine.namespaces['oval_defs_5'] + '}'):]
        if tag not in Component.comp_map:
            logger.critical('Unknown component tag: ' + comp_el.tag)
            import sys
            sys.exit()
        comp = Component.comp_map[tag]()
        comp.from_xml(parent, comp_el)
        return comp
