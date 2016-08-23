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
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_name': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}trustee_sid': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_delete': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_read_control': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_dac': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_owner': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_read': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_write': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_execute': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_query_conf': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_change_conf': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_query_stat': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_enum_dependents': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_start': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_stop': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_pause': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_interrogate': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_user_defined': {'class': 'oval_defs_5.EntityStateStringType'},
        }
    }
