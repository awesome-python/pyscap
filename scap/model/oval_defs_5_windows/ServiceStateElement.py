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
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}display_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}description',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}start_type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}current_state',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}controls_accepted',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}start_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}pid',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_flag',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dependencies',
        }
    }
