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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)

class Test(Model):
    @staticmethod
    def load(parent, test_el):
        from scap.model.oval_defs_5_windows.RegistryTest import RegistryTest
        from scap.model.oval_defs_5_windows.WUAUpdateSearcherTest import WUAUpdateSearcherTest
        test_map = {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_test': RegistryTest,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_test': WUAUpdateSearcherTest,
        }
        if test_el.tag not in test_map:
            logger.critical('Unknown Test tag: ' + test_el.tag)
            import sys
            sys.exit()
        test = test_map[test_el.tag]()
        test.from_xml(parent, test_el)
        return test

    # abstract
    def __init__(self):
        super(Test, self).__init__()

        self.check_existence = 'at_least_one_exists'
        self.check = None
        self.state_operator = 'AND'

        self.ignore_attributes.extend([
            'version',
            'comment',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated test ' + self.id)
        elif name == 'check_existence':
            self.check_existence = value
        elif name == 'check':
            self.check = value
        elif name == 'state_operator':
            self.state_operator = value
        else:
            return super(Test, self).parse_attribute(name, value)
        return True
