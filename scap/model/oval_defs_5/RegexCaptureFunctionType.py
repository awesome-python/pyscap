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
class RegexCaptureFunctionType(Model):
    MODEL_MAP = {
        'elements': {
            # from ComponentGroup
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}object_component': {'append': 'components', 'class': 'ObjectComponentType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variable_component': {'append': 'components', 'class': 'VariableComponentType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}literal_component': {'append': 'components', 'class': 'LiteralComponentType'},
            # from ComponentGroup/FunctionGroup
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}arithmetic': {'append': 'components', 'class': 'ArithmeticFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}begin': {'append': 'components', 'class': 'BeginFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}concat': {'append': 'components', 'class': 'ConcatFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}count': {'append': 'components', 'class': 'CountFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}end': {'append': 'components', 'class': 'EndFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}escape_regex': {'append': 'components', 'class': 'EscapeRegexFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}split': {'append': 'components', 'class': 'SplitFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}substring': {'append': 'components', 'class': 'SubstringFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}time_difference': {'append': 'components', 'class': 'TimeDifferenceFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}unique': {'append': 'components', 'class': 'UniqueFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}regex_capture': {'append': 'components', 'class': 'RegexCaptureFunctionType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}glob_to_regex': {'append': 'components', 'class': 'GlobToRegexFunctionType'},
        },
        'attributes': {
            'pattern': {'type': 'String'},
        }
    }
