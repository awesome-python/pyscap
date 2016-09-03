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
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_test': {'class': 'DpkgInfoTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_test': {'class': 'IfListenersTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_test': {'class': 'InetListeningServersTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_test': {'class': 'PartitionTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_test': {'class': 'RpmInfoTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_test': {'class': 'RpmVerifyFileTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_test': {'class': 'RpmVerifyPackageTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_test': {'class': 'RpmVerifyTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_test': {'class': 'SeLinuxBooleanTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_test': {'class': 'SeLinuxSecurityContextTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_test': {'class': 'SlackwarePkgInfoTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_test': {'class': 'SystemDUnitDependencyTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_test': {'class': 'SystemDUnitPropertyTestElement', 'min': 0, 'max': None},
}
OBJECT_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_object': {'class': 'DpkgInfoObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_object': {'class': 'IfListenersObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_object': {'class': 'InetListeningServersObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_object': {'class': 'PartitionObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_object': {'class': 'RpmInfoObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_object': {'class': 'RpmVerifyFileObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_object': {'class': 'RpmVerifyPackageObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_object': {'class': 'RpmVerifyObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_object': {'class': 'SeLinuxBooleanObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_object': {'class': 'SeLinuxSecurityContextObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_object': {'class': 'SlackwarePkgInfoObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_object': {'class': 'SystemDUnitDependencyObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_object': {'class': 'SystemDUnitPropertyObjectElement', 'min': 0, 'max': None},
}
STATE_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dpkginfo_state': {'class': 'DpkgInfoStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}iflisteners_state': {'class': 'IfListenersStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}inetlisteningservers_state': {'class': 'InetListeningServersStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}partition_state': {'class': 'PartitionStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpminfo_state': {'class': 'RpmInfoStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifyfile_state': {'class': 'RpmVerifyFileStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_state': {'class': 'RpmVerifyPackageStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverify_state': {'class': 'RpmVerifyStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxboolean_state': {'class': 'SeLinuxBooleanStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_state': {'class': 'SeLinuxSecurityContextStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}slackwarepkginfo_state': {'class': 'SlackwarePkgInfoStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitdependency_state': {'class': 'SystemDUnitDependencyStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}systemdunitproperty_state': {'class': 'SystemDUnitPropertyStateElement', 'min': 0, 'max': None},
}
