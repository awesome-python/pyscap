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
import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)
class Simple(Model):
    def __init__(self):
        super(Simple, self).__init__()
        self.id = None
        self.required_attributes = []

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

    def get_tag(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def get_text_element(self, tag, text):
        sub_el = ET.Element(tag)
        sub_el.text = text
        return sub_el

    def get_attributes(self):
        attribs = {}
        if self.id is not None:
            attribs['id'] = self.id
        return attribs

    # Template
    # def get_attributes(self):
    #     attribs = super(Simple, self).get_attributes()
    #
    #     return attribs
    #
    # def get_sub_elements(self):
    #     sub_els = super(Simple, self).get_sub_elements()
    #
    #     return sub_els

    def get_sub_elements(self):
        return []

    def to_xml(self):
        self.element = ET.Element(self.get_tag())


        for name, value in self.get_attributes().items():
            self.element.attrib[name] = value

        for attrib in self.required_attributes:
            if attrib not in self.element.attrib:
                logger.critical(self.__class__.__name__ + ' must define ' + attrib + ' attribute')
                import sys
                sys.exit()

        for sub_el in self.get_sub_elements():
            self.element.append(sub_el)

        return self.element
