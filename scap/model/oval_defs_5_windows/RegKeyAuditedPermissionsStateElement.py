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
class RegKeyAuditedPermissionsStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'regkeyauditedpermissions_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}hive': {'class': 'EntityStateRegistryHiveType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}trustee_name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_delete': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_read_control': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_owner': {'class': 'EntityStateAuditType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_dac': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_synchronize': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_system_security': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_read': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_write': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_execute': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_all': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_query_value': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_set_value': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_create_sub_key': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_enumerate_sub_keys': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_notify': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_create_link': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_wow64_64key': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_wow64_32key': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key_wow64_res': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}windows_view': {'class': 'EntityStateWindowsViewType', 'min': 0},
        }
    }
