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
TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_test': {'class': 'DPKGInfoTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_test': {'class': 'IFListenersTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_test': {'class': 'InetListeningServersTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_test': {'class': 'PartitionTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_test': {'class': 'RPMInfoTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_test': {'class': 'RPMVerifyFileTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_test': {'class': 'RPMVerifyPackageTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_test': {'class': 'RPMVerifyTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_test': {'class': 'SELinuxBooleanTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_test': {'class': 'SELinuxSecurityContextTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_test': {'class': 'SlackwarePkgInfoTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_test': {'class': 'SystemDUnitDependencyTestType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_test': {'class': 'SystemDUnitPropertyTestType'},

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_object': {'class': 'DPKGInfoObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_object': {'class': 'IFListenersObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_object': {'class': 'InetListeningServersObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_object': {'class': 'PartitionObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_object': {'class': 'RPMInfoObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_object': {'class': 'RPMVerifyFileObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_object': {'class': 'RPMVerifyPackageObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_object': {'class': 'RPMVerifyObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_object': {'class': 'SELinuxBooleanObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_object': {'class': 'SELinuxSecurityContextObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_object': {'class': 'SlackwarePkgInfoObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_object': {'class': 'SystemDUnitDependencyObjectType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_object': {'class': 'SystemDUnitPropertyObjectType'},

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_state': {'class': 'DPKGInfoStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_state': {'class': 'IFListenersStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_state': {'class': 'InetListeningServersStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_state': {'class': 'PartitionStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_state': {'class': 'RPMInfoStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_state': {'class': 'RPMVerifyFileStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_state': {'class': 'RPMVerifyPackageStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_state': {'class': 'RPMVerifyStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_state': {'class': 'SELinuxBooleanStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_state': {'class': 'SELinuxSecurityContextStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_state': {'class': 'SlackwarePkgInfoStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_state': {'class': 'SystemDUnitDependencyStateType'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_state': {'class': 'SystemDUnitPropertyStateType'},
}
