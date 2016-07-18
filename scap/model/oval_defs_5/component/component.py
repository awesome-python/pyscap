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

from scap.model.content import Content
import logging
from scap.engine.engine import Engine

from scap.model.oval_defs_5.component.object_component import ObjectComponent
from scap.model.oval_defs_5.component.variable_component import VariableComponent
from scap.model.oval_defs_5.component.literal_component import LiteralComponent
from scap.model.oval_defs_5.component.functions_group import FunctionsGroup

from scap.model.oval_defs_5.component.function.arithmetic import ArithmeticFunction
from scap.model.oval_defs_5.component.function.begin import BeginFunction
from scap.model.oval_defs_5.component.function.concat import ConcatFunction
from scap.model.oval_defs_5.component.function.count import CountFunction
from scap.model.oval_defs_5.component.function.end import EndFunction
from scap.model.oval_defs_5.component.function.escape_regex import EscapeRegexFunction
from scap.model.oval_defs_5.component.function.split import SplitFunction
from scap.model.oval_defs_5.component.function.substring import SubstringFunction
from scap.model.oval_defs_5.component.function.time_difference import TimeDifferenceFunction
from scap.model.oval_defs_5.component.function.unique import UniqueFunction
from scap.model.oval_defs_5.component.function.regex_capture import RegexCaptureFunction

logger = logging.getLogger(__name__)
class Component(Content):
    comp_map = {
        'object_component': ObjectComponent,
        'variable_component': VariableComponent,
        'literal_component': LiteralComponent,
        'functions': FunctionsGroup,

        'arithmetic': ArithmeticFunction,
        'begin': BeginFunction,
        'concat': ConcatFunction,
        'count': CountFunction,
        'end': EndFunction,
        'escape_regex': EscapeRegexFunction,
        'split': SplitFunction,
        'substring': SubstringFunction,
        'time_difference': TimeDifferenceFunction,
        'unique': UniqueFunction,
        'regex_capture': RegexCaptureFunction,
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
        return Component.comp_map[tag](parent, comp_el)
