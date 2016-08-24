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
class FileAuditedPermissions53StateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'fileauditedpermissions53_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filename': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}trustee_sid': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_delete': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_read_control': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_dac': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_owner': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_synchronize': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_system_security': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_read': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_write': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_execute': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_all': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_data': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_write_data': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_append_data': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_ea': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_write_ea': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_execute': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_delete_child': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_attributes': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_write_attributes': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}windows_view': {'class': 'EntityStateWindowsViewType', 'min': 0},
        }
    }
