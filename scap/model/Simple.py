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
class Simple(Model):
    def from_xml(self, parent, el, ref_mapping=None):
        super(Simple, self).from_xml(parent, el, ref_mapping)

        for name, value in el.attrib.items():
            if not self.parse_attrib(name, value):
                logger.critical('Unknown attrib in ' + el.tag + ': ' + name + ' = ' + value)
                import sys
                sys.exit()

        for sub_el in el:
            if not self.parse_sub_el(sub_el):
                logger.critical('Unknown element in ' + el.tag + ': ' + sub_el.tag)
                import sys
                sys.exit()

    def parse_attrib(self, name, value):
        if name == '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation':
            pass
        elif name == '{http://www.w3.org/XML/1998/namespace}lang':
            pass
        elif name == '{http://www.w3.org/XML/1998/namespace}base':
            pass
        elif name == 'id':
            self.id = value
        else:
            return False
        return True

    def parse_sub_el(self, sub_el):
        return False

    def parse_boolean(self, value):
        if value == 'true' or value == '1':
            return True
        else:
            return False
