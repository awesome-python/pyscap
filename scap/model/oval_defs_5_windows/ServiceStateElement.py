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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class ServiceStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'service_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}display_name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}description': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_type': {'class': 'EntityStateServiceTypeType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}start_type': {'class': 'EntityStateServiceStartTypeType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}current_state': {'class': 'EntityStateServiceCurrentStateType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}controls_accepted': {'class': 'EntityStateServiceControlsAcceptedType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}start_name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}pid': {'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_flag': {'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dependencies': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
        }
    }
