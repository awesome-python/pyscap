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
    def __init__(self, value=None):
        super(Simple, self).__init__()

        if value is None:
            self.value = None
        else:
            self.parse_value(value)

    def parse_value(self, value):
        self.value = value
        return self.value

    def is_none(self):
        return self.value is None

    def __str__(self):
        return str(self.value)

    def from_xml(self, parent, sub_el):
        super(Simple, self).from_xml(parent, sub_el)

        if sub_el.text:
            self.parse_value(sub_el.text)
        else:
            self.value = None

    def to_xml(self):
        el = ET.Element(self.get_tag())

        for name in self.model_map['attributes']:
            self.produce_attribute(name, el)

        # should be no subelements as a Simple

        if not self.is_none():
            el.text = str(self)

        return el
