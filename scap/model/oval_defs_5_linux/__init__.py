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
TEST_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_test': {'class': 'DPKGInfoTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_test': {'class': 'IFListenersTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_test': {'class': 'InetListeningServersTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_test': {'class': 'PartitionTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_test': {'class': 'RPMInfoTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_test': {'class': 'RPMVerifyFileTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_test': {'class': 'RPMVerifyPackageTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_test': {'class': 'RPMVerifyTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_test': {'class': 'SELinuxBooleanTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_test': {'class': 'SELinuxSecurityContextTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_test': {'class': 'SlackwarePkgInfoTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_test': {'class': 'SystemDUnitDependencyTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_test': {'class': 'SystemDUnitPropertyTestElement'},
}
OBJECT_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_object': {'class': 'DPKGInfoObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_object': {'class': 'IFListenersObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_object': {'class': 'InetListeningServersObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_object': {'class': 'PartitionObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_object': {'class': 'RPMInfoObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_object': {'class': 'RPMVerifyFileObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_object': {'class': 'RPMVerifyPackageObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_object': {'class': 'RPMVerifyObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_object': {'class': 'SELinuxBooleanObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_object': {'class': 'SELinuxSecurityContextObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_object': {'class': 'SlackwarePkgInfoObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_object': {'class': 'SystemDUnitDependencyObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_object': {'class': 'SystemDUnitPropertyObjectElement'},
}
STATE_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_state': {'class': 'DPKGInfoStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_state': {'class': 'IFListenersStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_state': {'class': 'InetListeningServersStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_state': {'class': 'PartitionStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_state': {'class': 'RPMInfoStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_state': {'class': 'RPMVerifyFileStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_state': {'class': 'RPMVerifyPackageStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_state': {'class': 'RPMVerifyStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_state': {'class': 'SELinuxBooleanStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_state': {'class': 'SELinuxSecurityContextStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_state': {'class': 'SlackwarePkgInfoStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_state': {'class': 'SystemDUnitDependencyStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_state': {'class': 'SystemDUnitPropertyStateElement'},
}
