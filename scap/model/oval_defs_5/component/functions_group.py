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
class FunctionsGroup(Component):
    def __init__(self, parent, el):
        super(self.__class__, self).__init__(parent, el)

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
        self.components = []
        for comp_el in el:
            if comp_el.tag.endswith('arithmetic'):
                self.components.append(ArithmeticFunction(self, comp_el))
            elif comp_el.tag.endswith('begin'):
                self.components.append(BeginFunction(self, comp_el))
            elif comp_el.tag.endswith('concat'):
                self.components.append(ConcatFunction(self, comp_el))
            elif comp_el.tag.endswith('count'):
                self.components.append(CountFunction(self, comp_el))
            elif comp_el.tag.endswith('end'):
                self.components.append(EndFunction(self, comp_el))
            elif comp_el.tag.endswith('escape_regex'):
                self.components.append(EscapeRegexFunction(self, comp_el))
            elif comp_el.tag.endswith('split'):
                self.components.append(SplitFunction(self, comp_el))
            elif comp_el.tag.endswith('substring'):
                self.components.append(SubstringFunction(self, comp_el))
            elif comp_el.tag.endswith('time_difference'):
                self.components.append(TimeDifferenceFunction(self, comp_el))
            elif comp_el.tag.endswith('unique'):
                self.components.append(UniqueFunction(self, comp_el))
            elif comp_el.tag.endswith('regex_capture'):
                self.components.append(RegexCaptureFunction(self, comp_el))
            else:
                logger.critical('Unknown component in functions group: ' + comp_el.tag)
                import sys
                sys.exit()
