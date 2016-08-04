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

logger = logging.getLogger(__name__)
class ComponentGroupType(Model):
    TAG_MAP = {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}object_component': {'class': 'ObjectComponentType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variable_component': {'class': 'VariableComponentType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}literal_component': {'class': 'LiteralComponentType'},

            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}arithmetic': {'class': 'ArithmeticFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}begin': {'class': 'BeginFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}concat': {'class': 'ConcatFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}count': {'class': 'CountFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}end': {'class': 'EndFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}escape_regex': {'class': 'EscapeRegexFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}split': {'class': 'SplitFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}substring': {'class': 'SubstringFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}time_difference': {'class': 'TimeDifferenceFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}unique': {'class': 'UniqueFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}regex_capture': {'class': 'RegexCaptureFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}glob_to_regex': {'class': 'GlobToRegexFunctionType'},
    }
    def __init__(self):
        super(ComponentGroupType, self).__init__()

        self.components = []

    def parse_element(self, sub_el):
        sub_el_tags = {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}object_component': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variable_component': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}literal_component': True,

            # collapse FunctionGroup into ComponentGroup
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}arithmetic': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}begin': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}concat': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}count': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}end': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}escape_regex': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}split': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}substring': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}time_difference': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}unique': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}regex_capture': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}glob_to_regex': True,
        }

        if sub_el.tag in sub_el_tags:
            self.components.append(Model.load(self, sub_el))
        else:
            return super(ComponentGroupType, self).parse_element(sub_el)
        return True
