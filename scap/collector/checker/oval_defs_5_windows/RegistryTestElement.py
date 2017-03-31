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

from scap.collector.checker.oval_defs_5_windows.TestType import TestType

logger = logging.getLogger(__name__)
class RegistryTestElement(TestType):
    def collect_object_items(self):
        obj = self.resolve_reference(self.content.object.object_ref)
        if obj.set':
            raise NotImplementedError('Sets are not implemented')

        fullkey = obj.hive.get_text()

        if obj.key is not None:
            fullkey += '\\' + obj.key.get_text()

        args = ['QUERY', '"' + fullkey + '"']

        if obj.name is None:
            args.extend(['/ve'])
        else:
            args.extend(['/v', '"' + obj.name.get_text() + '"'])

        if obj.behaviors:
            #TODO: max_depth registry behavior cannot be implemented using reg.exe
            if obj.behaviors.max_depth != -1:
                logger.warning('max_depth registry behavior cannot be implemented using reg.exe')

            #TODO: recurse_direction registry behavior cannot be implemented using reg.exe
            if obj.behaviors.recurse_direction != 'none':
                logger.warning('recurse_direction registry behavior cannot be implemented using reg.exe')

            if obj.behaviors.windows_view == '32_bit':
                args.extend(['/reg:32'])
            elif obj.behaviors.windows_view == '64_bit':
                args.extend(['/reg:64'])
            else:
                raise ValueError("Unknown windows view: " + obj.behaviors.windows_view)

        lines = self.host.exec_command('REG', tuple(args))

        items = []
        existence = []
        for line in lines:
            line = line.strip('\r\n')
            if line == '':
                continue

            if re.match('ERROR: The system was unable to find', line):
                return [{}], ['does not exist']

            elif re.match('\s+', line):
                # value line: name, type, value
                line = re.split('\s+', line)
                item['name'] = line[1]
                item['type'] = line[2]
                item['value'] = line[3]
                items.append(item)
                existence.append('exists')

            else:
                # hk, path line
                line = line.split('\\')
                item = {
                    'hive': line[0],
                    'key': '\\'.join(line[1:]),
                }

        logger.debug('Found object items: ' + str(items) + ' (' + str(existence) + ')')

        return items, existence

    def compare_item_state(self, item, state):
        #TODO no way to validate windows_view
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
