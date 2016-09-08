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

import logging
import re

from scap.checker.oval_defs_5_windows.TestType import TestType

logger = logging.getLogger(__name__)
class RegistryTestElement(TestType):
    # HIVE_XLATE = {
    #     'HKEY_CLASSES_ROOT': 'HKCR',
    #     'HKEY_CURRENT_CONFIG': 'HKCC',
    #     'HKEY_CURRENT_USER': 'HKCU',
    #     'HKEY_LOCAL_MACHINE': 'HKLM',
    #     'HKEY_USERS': 'HKU',
    # }

    def collect_object_items(self):
        if hasattr(self.content, 'set'):
            raise NotImplementedError('Sets are not implemented')
        if hasattr(self.content, 'behaviors'):
            raise NotImplementedError('RegistryBehaviors are not implemented')

        obj = self.resolve_reference(self.content.object.object_ref)

        fullkey = obj.hive.get_text() + '\\' + obj.key.get_text()
        args = ['QUERY', '"' + fullkey + '"']
        if not obj.name is None:
            args.extend(['/v', '"' + obj.name.get_text() + '"'])
        for line in self.host.lines_from_command('REG', tuple(args)):
            line = line.strip('\r\n')
            if line == '':
                continue
            #logger.debug(line)

            if re.match('\s+', line):
                # value line: name, type, value
                value = re.split('\s+', line)
                logger.debug(str())
            else:
                # path line
                logger.debug(str(line.split('\\')))



    def eval_item_state(self, item, state):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
