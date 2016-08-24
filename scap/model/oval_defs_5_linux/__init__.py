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
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_test': {'class': 'DpkgInfoTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_test': {'class': 'IfListenersTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_test': {'class': 'InetListeningServersTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_test': {'class': 'PartitionTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_test': {'class': 'RpmInfoTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_test': {'class': 'RpmVerifyFileTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_test': {'class': 'RpmVerifyPackageTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_test': {'class': 'RpmVerifyTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_test': {'class': 'SeLinuxBooleanTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_test': {'class': 'SeLinuxSecurityContextTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_test': {'class': 'SlackwarePkgInfoTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_test': {'class': 'SystemDUnitDependencyTestElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_test': {'class': 'SystemDUnitPropertyTestElement'},
}
OBJECT_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_object': {'class': 'DpkgInfoObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_object': {'class': 'IfListenersObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_object': {'class': 'InetListeningServersObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_object': {'class': 'PartitionObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_object': {'class': 'RpmInfoObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_object': {'class': 'RpmVerifyFileObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_object': {'class': 'RpmVerifyPackageObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_object': {'class': 'RpmVerifyObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_object': {'class': 'SeLinuxBooleanObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_object': {'class': 'SeLinuxSecurityContextObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_object': {'class': 'SlackwarePkgInfoObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_object': {'class': 'SystemDUnitDependencyObjectElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_object': {'class': 'SystemDUnitPropertyObjectElement'},
}
STATE_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_state': {'class': 'DpkgInfoStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_state': {'class': 'IfListenersStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_state': {'class': 'InetListeningServersStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_state': {'class': 'PartitionStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_state': {'class': 'RpmInfoStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_state': {'class': 'RpmVerifyFileStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_state': {'class': 'RpmVerifyPackageStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_state': {'class': 'RpmVerifyStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_state': {'class': 'SeLinuxBooleanStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_state': {'class': 'SeLinuxSecurityContextStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_state': {'class': 'SlackwarePkgInfoStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_state': {'class': 'SystemDUnitDependencyStateElement'},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_state': {'class': 'SystemDUnitPropertyStateElement'},
}
