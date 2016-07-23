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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Model(object):
    @staticmethod
    def load(content):
        root = content.getroot()
        from scap.Engine import Engine
        if root.tag.startswith('{' + Engine.namespaces['scap_1_2']):
            from scap.model.scap_1_2.DataStreamCollection import DataStreamCollection
            dsc = DataStreamCollection()
            dsc.from_xml(None, root)
            return dsc
        else:
            logger.critical('Unsupported content with root namespace: ' + str(content.get_root_namespace()))
            sys.exit()

    def __init__(self):
        self.parent = None
        self.element = None
        self.ref_mapping = {}

        self.id = None
        self.required_attributes = []
        self.ignore_attributes = []
        self.ignore_sub_elements = []
        self.tag_name = None

    def from_xml(self, parent, el):
        self.parent = parent
        self.element = el

        for name, value in el.attrib.items():
            if not self.parse_attribute(name, value):
                logger.critical('Unknown attrib in ' + el.tag + ': ' + name + ' = ' + value)
                import sys
                sys.exit()

        for sub_el in el:
            if not self.parse_sub_el(sub_el):
                logger.critical('Unknown element in ' + el.tag + ': ' + sub_el.tag)
                import sys
                sys.exit()

    def parse_attribute(self, name, value):
        if name == '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation':
            pass
        elif name == '{http://www.w3.org/XML/1998/namespace}lang':
            pass
        elif name == '{http://www.w3.org/XML/1998/namespace}base':
            pass
        elif name == 'id':
            self.id = value
        elif name in self.ignore_attributes:
            pass
        else:
            return False
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag in self.ignore_sub_elements:
            return True
        return False

    # Template
    # def parse_attribute(self, name, value):
    #     if name == 'tag':
    #         self.tag = value
    #     else:
    #         return super(SubClass, self).parse_attribute(name, value)
    #     return True
    #
    # def parse_sub_el(self, sub_el):
    #     if sub_el.tag == '{namespace}tag':
    #         self.tags.append(sub_el.tag)
    #     else:
    #         return super(SubClass, self).parse_sub_el(sub_el)
    #     return True

    def parse_boolean(self, value):
        if value == 'true' or value == '1':
            return True
        else:
            return False

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            ref = self.ref_mapping[ref]

        if not self.parent:
            raise RuntimeError("Got to null parent without resolving reference")

        return self.parent.resolve_reference(ref)

    def set_ref_mapping(self, mapping):
        logger.debug('Updating reference mapping with ' + str(mapping))
        self.ref_mapping.update(mapping)

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
    #     attribs = super(Model, self).get_attributes()
    #
    #     return attribs
    #
    # Template
    # def get_sub_elements(self):
    #     sub_els = super(Model, self).get_sub_elements()
    #
    #     return sub_els

    def get_sub_elements(self):
        return []

    def to_xml(self):
        if self.element is None:
            if self.tag_name is None:
                raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag_name')
            self.element = ET.Element(self.tag_name)

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
