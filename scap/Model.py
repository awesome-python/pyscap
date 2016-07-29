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
    namespaces = {
        'http://scap.nist.gov/schema/asset-identification/1.1': 'ai_1_1',
        'http://scap.nist.gov/schema/asset-reporting-format/1.1': 'arf_1_1',
        'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0': 'arf_rel_1_0',
        'http://cpe.mitre.org/dictionary/2.0': 'cpe_dict_2_0',
        'http://cpe.mitre.org/language/2.0': 'cpe_lang_2_0',
        'http://purl.org/dc/elements/1.1/': 'dc_el_1_1',
        'http://scap.nist.gov/schema/ocil/2.0': 'ocil_2_0',
        'http://scap.nist.gov/schema/ocil/2': 'ocil_2',
        'http://oval.mitre.org/XMLSchema/oval-common-5': 'oval_common_5',
        'http://oval.mitre.org/XMLSchema/oval-definitions-5': 'oval_defs_5',
        'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent': 'oval_defs_5_independent',
        'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux': 'oval_defs_5_linux',
        'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows': 'oval_defs_5_windows',
        'http://scap.nist.gov/schema/scap/source/1.2': 'scap_1_2',
        'http://scap.nist.gov/schema/reporting-core/1.1': 'rep_core_1_1',
        'http://checklists.nist.gov/xccdf/1.1': 'xccdf_1_1',
        'http://checklists.nist.gov/xccdf/1.2': 'xccdf_1_2',
        'http://www.w3.org/1999/xhtml': 'xhtml',
        'http://www.w3.org/1999/xlink': 'xlink',
        'urn:oasis:names:tc:entity:xmlns:xml:catalog': 'xml_cat',
        'http://scap.nist.gov/schema/xml-dsig/1.0': 'xml_dsig_1_0',
        'http://www.w3.org/2001/XMLSchema-instance': 'xml_schema_instance',
        'http://www.w3.org/2000/09/xmldsig#': 'xmldsig_2000_09',
        'http://www.w3.org/2001/XMLSchema': 'xsd',
    }

    @staticmethod
    def parse_tag(tag):
        # parse tag
        xml_namespace, tag_name = tag[1:].split('}')

        if xml_namespace not in Model.namespaces:
            logger.critical('Unsupported ' + tag_name + ' tag with namespace: ' + xml_namespace)
            import sys
            sys.exit()
        model_namespace = Model.namespaces[xml_namespace]

        module_name = tag_name.replace('-', '_')
        import keyword
        if keyword.iskeyword(module_name):
            module_name += '_'

        return xml_namespace, model_namespace, tag_name, module_name

    @staticmethod
    def load_child(parent, child_el):
        xml_namespace, model_namespace, tag_name, module_name = Model.parse_tag(child_el.tag)

        model_module = 'scap.model.' + model_namespace + '.' + module_name

        # try to load the tag's module
        import sys
        if model_module not in sys.modules:
            logger.debug('Loading module ' + model_module)
            import importlib
            mod = importlib.import_module(model_module)
        else:
            mod = sys.modules[model_module]

        # instantiate an instance of the class & load it
        inst = eval('mod.' + module_name + '()')
        inst.xml_namespace = xml_namespace
        inst.model_namespace = model_namespace
        inst.tag_name = tag_name
        inst.from_xml(parent, child_el)

        return inst

    # tag must be defined for models using to_xml; the tag information is automatically parsed by from_xml
    def __init__(self, tag=None):
        if tag is None:
            self.xml_namespace = None
            self.model_namespace = None
            self.tag_name = None
        else:
            self.xml_namespace, self.model_namespace, self.tag_name, module_name = Model.parse_tag(tag)

        self.parent = None
        self.element = None
        self.ref_mapping = {}

        self.id = None
        self.required_attributes = []
        self.ignore_attributes = []
        self.required_sub_elements = []
        self.ignore_sub_elements = []

    def get_tag(self):
        if self.tag_name is None or self.xml_namespace is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag')
        return '{' + self.xml_namespace + '}' + self.tag_name

    def get_xml_namespace(self):
        if self.xml_namespace is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag')
        return self.xml_namespace

    def from_xml(self, parent, el):
        self.parent = parent
        self.element = el

        if self.xml_namespace is None or self.model_namespace is None or self.tag_name is None:
            self.xml_namespace, self.model_namespace, self.tag_name, module_name = Model.parse_tag(el.tag)

        for attrib in self.required_attributes:
            if attrib not in self.element.attrib:
                logger.critical(el.tag + ' must define ' + attrib + ' attribute')
                import sys
                sys.exit()

        for name, value in el.attrib.items():
            if not self.parse_attribute(name, value):
                logger.critical('Unknown attrib in ' + el.tag + ': ' + name + ' = ' + value)
                import sys
                sys.exit()

        parsed_sub_elements = []
        for sub_el in el:
            if not self.parse_sub_el(sub_el):
                logger.critical('Unknown element in ' + el.tag + ': ' + sub_el.tag)
                import sys
                sys.exit()
            parsed_sub_elements.append(sub_el.tag)

        for sub_el_tag in self.required_sub_elements:
            if sub_el_tag not in parsed_sub_elements:
                logger.critical(el.tag + ' does not contain a required sub element: ' + sub_el_tag)
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

    # Template
    # def parse_attribute(self, name, value):
    #     if name == 'tag':
    #         self.tag = value
    #     else:
    #         return super(SubClass, self).parse_attribute(name, value)
    #     return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag in self.ignore_sub_elements:
            return True
        return False

    # Template
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

    # Template
    # def get_sub_elements(self):
    #     sub_els = super(Model, self).get_sub_elements()
    #
    #     return sub_els

    def get_sub_elements(self):
        return []

    def to_xml(self, tag=None):
        if tag is not None:
            self.xml_namespace, self.model_namespace, self.tag_name, module_name = Model.parse_tag(tag)
        elif self.tag_name is None or self.xml_namespace is None:
            logger.critical(self.__class__.__name__ + ' has not defined a tag before production of xml')
            import sys
            sys.exit()

        if self.element is None:
            self.element = ET.Element(self.get_tag())

            for name, value in self.get_attributes().items():
                self.element.attrib[name] = value

            for attrib in self.required_attributes:
                if attrib not in self.element.attrib:
                    logger.critical(self.__class__.__name__ + ' must define ' + attrib + ' attribute')
                    import sys
                    sys.exit()

            produced_sub_elements = []
            for sub_el in self.get_sub_elements():
                self.element.append(sub_el)
                produced_sub_elements.append(sub_el.tag)

            for sub_el_tag in self.required_sub_elements:
                if sub_el_tag not in produced_sub_elements:
                    logger.critical(self.element.tag + ' does not contain a required sub element: ' + sub_el_tag)
                    import sys
                    sys.exit()
        return self.element
