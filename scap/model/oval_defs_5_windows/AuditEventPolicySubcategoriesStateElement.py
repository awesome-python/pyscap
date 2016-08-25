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

class AuditEventPolicySubcategoriesStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'auditeventpolicysubcategories_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}credential_validation': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kerberos_authentication_service': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kerberos_service_ticket_operations': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kerberos_ticket_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_account_logon_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}application_group_management': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}computer_account_management': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}distribution_group_management': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_account_management_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_group_management': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_account_management': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dpapi_activity': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_creation': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_termination': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}rpc_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}directory_service_access': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}directory_service_changes': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}directory_service_replication': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}detailed_directory_service_replication': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}account_lockout': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_extended_mode': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_main_mode': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_quick_mode': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logoff': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logon': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}network_policy_server': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_logon_logoff_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}special_logon': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logon_claims': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}application_generated': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}certification_services': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}detailed_file_share': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_share': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_system': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filtering_platform_connection': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filtering_platform_packet_drop': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}handle_manipulation': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kernel_object': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_object_access_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sam': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}removable_storage': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}central_access_policy_staging': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}audit_policy_change': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}authentication_policy_change': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}authorization_policy_change': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filtering_platform_policy_change': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}mpssvc_rule_level_policy_change': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_policy_change_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}non_sensitive_privilege_use': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_privilege_use_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sensitive_privilege_use': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_driver': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_system_events': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_state_change': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_system_extension': {'class': 'EntityStateAuditType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}system_integrity': {'class': 'EntityStateAuditType', 'min': 0},
        }
    }
