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

from scap.model.oval_defs_5_windows.State import State
import logging

logger = logging.getLogger(__name__)

class auditeventpolicysubcategories_state(State):
    def __init__(self):
        super(auditeventpolicysubcategories_state, self).__init__(
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_state')

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}credential_validation',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kerberos_authentication_service',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kerberos_service_ticket_operations',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kerberos_ticket_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_account_logon_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}application_group_management',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}computer_account_management',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}distribution_group_management',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_account_management_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_group_management',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_account_management',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dpapi_activity',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_creation',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_termination',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}rpc_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}directory_service_access',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}directory_service_changes',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}directory_service_replication',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}detailed_directory_service_replication',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}account_lockout',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_extended_mode',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_main_mode',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_quick_mode',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logoff',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logon',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}network_policy_server',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_logon_logoff_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}special_logon',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logon_claims',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}application_generated',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}certification_services',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}detailed_file_share',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_share',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_system',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filtering_platform_connection',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filtering_platform_packet_drop',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}handle_manipulation',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}kernel_object',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_object_access_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sam',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}removable_storage',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}central_access_policy_staging',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}audit_policy_change',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}authentication_policy_change',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}authorization_policy_change',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filtering_platform_policy_change',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}mpssvc_rule_level_policy_change',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_policy_change_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}non_sensitive_privilege_use',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_privilege_use_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sensitive_privilege_use',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ipsec_driver',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}other_system_events',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_state_change',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_system_extension',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}system_integrity',
        ])
