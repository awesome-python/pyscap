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

    def _parse_reg(self, lines):
        item = {}
        for line in lines:
            line = line.strip('\r\n')
            if line == '':
                continue
            #logger.debug(line)

            if re.match('ERROR: The system was unable to find', line):
                return {}, 'does not exist'
            elif re.match('\s+', line):
                # value line: name, type, value
                line = re.split('\s+', line)
                item['name'] = line[1]
                item['type'] = line[2]
                item['value'] = line[3]
                return item, 'exists'
            else:
                # hk, path line
                line = line.split('\\')
                item['hive'] = line[0]
                item['key'] = '\\'.join(line[1:])

    def collect_object_items(self):
        items = []
        existence = []

        obj = self.resolve_reference(self.content.object.object_ref)
        if hasattr(obj, 'set'):
            raise NotImplementedError('Sets are not implemented')
        if hasattr(obj, 'behaviors'):
            raise NotImplementedError('RegistryBehaviors are not implemented')

        fullkey = obj.hive.get_text() + '\\' + obj.key.get_text()
        args = ['QUERY', '"' + fullkey + '"']
        if obj.name is not None:
            args.extend(['/v', '"' + obj.name.get_text() + '"'])

        lines = self.host.lines_from_command('REG', tuple(args))
        item, exists = self._parse_reg(lines)
        logger.debug('Found object item: ' + str(item) + ' (' + exists + ')')
        items.append(item)
        existence.append(exists)

        return items, existence

    def eval_item_state(self, item, state):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
