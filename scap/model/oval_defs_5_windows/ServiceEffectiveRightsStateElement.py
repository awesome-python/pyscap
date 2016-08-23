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
class ServiceEffectiveRightsStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'serviceeffectiverights_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}trustee_sid',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_delete',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_read_control',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_dac',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_owner',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_read',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_write',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_execute',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_query_conf',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_change_conf',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_query_stat',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_enum_dependents',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_start',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_stop',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_pause',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_interrogate',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_user_defined',
        }
    }
