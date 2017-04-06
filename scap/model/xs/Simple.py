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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Simple(Model):
    def __init__(self):
        super(Simple, self).__init__()

        self.value = None

    def parse_value(self, value):
        return value

    def from_xml(self, parent, sub_el):
        super(Simple, self).from_xml(parent, sub_el)

        if sub_el.text:
            self.value = sub_el.text
        else:
            self.value = ''

    def to_xml(self):
        el = ET.Element(self.get_tag())

        for name in self.model_map['attributes']:
            value = self.produce_attribute(name)
            if value is not None:
                el.set(name, value)

        for tag in self.model_map['elements']:
            el.extend(self.produce_sub_elements(tag))

        if self.value is not None:
            if isinstance(self.value, bytes):
                logger.warning(self.__class__.__name__ + ' has bytes type as value')
            el.text = self.value

        return el
