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
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_test': {'class': 'EnvironmentVariableTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable58_test': {'class': 'EnvironmentVariable58TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_test': {'class': 'FamilyTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash58_test': {'class': 'FileHash58TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_test': {'class': 'FileHashTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap57_test': {'class': 'LDAP57TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap_test': {'class': 'LDAPTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql57_test': {'class': 'SQL57TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_test': {'class': 'SQLTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent54_test': {'class': 'TextFileContent54TestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_test': {'class': 'TextFileContentTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}unknown_test': {'class': 'UnknownTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_test': {'class': 'VariableTestElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_test': {'class': 'XMLFileContentTestElement', 'min': 0, 'max': None},
}
OBJECT_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_object': {'class': 'EnvironmentVariableObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable58_object': {'class': 'EnvironmentVariable58ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_object': {'class': 'FamilyObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash58_object': {'class': 'FileHash58ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_object': {'class': 'FileHashObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap57_object': {'class': 'LDAP57ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap_object': {'class': 'LDAPObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql57_object': {'class': 'SQL57ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_object': {'class': 'SQLObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent54_object': {'class': 'TextFileContent54ObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_object': {'class': 'TextFileContentObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_object': {'class': 'VariableObjectElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_object': {'class': 'XMLFileContentObjectElement', 'min': 0, 'max': None},
}
STATE_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_state': {'class': 'EnvironmentVariableStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable58_state': {'class': 'EnvironmentVariable58StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_state': {'class': 'FamilyStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash58_state': {'class': 'FileHash58StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_state': {'class': 'FileHashStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap57_state': {'class': 'LDAP57StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap_state': {'class': 'LDAPStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql57_state': {'class': 'SQL57StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_state': {'class': 'SQLStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent54_state': {'class': 'TextFileContent54StateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_state': {'class': 'TextFileContentStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_state': {'class': 'VariableStateElement', 'min': 0, 'max': None},
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_state': {'class': 'XMLFileContentStateElement', 'min': 0, 'max': None},
}
