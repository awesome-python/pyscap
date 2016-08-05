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
    NAMESPACES = {
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
        'http://oval.mitre.org/XMLSchema/oval-results-5': 'oval_results_5',
        'http://scap.nist.gov/schema/scap/source/1.2': 'scap_1_2',
        'http://scap.nist.gov/schema/reporting-core/1.1': 'rep_core_1_1',
        'http://checklists.nist.gov/xccdf/1.1': 'xccdf_1_1',
        'http://checklists.nist.gov/xccdf/1.2': 'xccdf_1_2',
        'http://www.w3.org/1999/xhtml': 'xhtml',
        'http://www.w3.org/1999/xlink': 'xlink',
        'urn:oasis:names:tc:entity:xmlns:xml:catalog': 'xml_cat',
        'http://scap.nist.gov/schema/xml-dsig/1.0': 'xml_dsig_1_0',
        'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
        'http://www.w3.org/2000/09/xmldsig#': 'xmldsig_2000_09',
        'http://www.w3.org/2001/XMLSchema': 'xs',
        'http://www.w3.org/XML/1998/namespace': 'xml'
    }

    ATTRIBUTE_MAP = {
        '{http://www.w3.org/XML/1998/namespace}lang': {'ignore': True},
        '{http://www.w3.org/XML/1998/namespace}base': {'ignore': True},
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': {'ignore': True},
    }

    class_attribute_maps = {}
    class_tag_maps = {}

    @staticmethod
    def parse_tag(tag):
        # parse tag
        if tag[0] == '{':
            xml_namespace, tag_name = tag[1:].split('}')
        else:
            return None, None, tag

        if xml_namespace not in Model.NAMESPACES:
            logger.critical('Unsupported ' + tag_name + ' tag with namespace: ' + xml_namespace)
            import sys
            sys.exit()
        model_namespace = Model.NAMESPACES[xml_namespace]

        return xml_namespace, model_namespace, tag_name

    @staticmethod
    def load(parent, child_el):
        xml_namespace, model_namespace, tag_name = Model.parse_tag(child_el.tag)

        # try to load the tag's module
        import sys, importlib
        if parent is None:
            # look up from __init__ file
            pkg_mod = importlib.import_module('scap.model.' + model_namespace)
            try:
                module_name = pkg_mod.TAG_MAP[child_el.tag]['class']
            except AttributeError:
                sys.exit(pkg_mod.__name__ + ' does not define TAG_MAP')
            except KeyError:
                sys.exit(pkg_mod.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')
        else:
            try:
                module_name = parent.__class__.TAG_MAP[child_el.tag]['class']
            except AttributeError:
                sys.exit(parent.__class__.__name__ + ' does not define TAG_MAP')
            except KeyError:
                sys.exit(parent.__class__.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')
        model_module = 'scap.model.' + model_namespace + '.' + module_name
        if model_module not in sys.modules:
            logger.debug('Loading module ' + model_module)

            mod = importlib.import_module(model_module)
        else:
            mod = sys.modules[model_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, module_name)
        inst = class_()
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
            self.xml_namespace, self.model_namespace, self.tag_name = Model.parse_tag(tag)

        self.parent = None
        self.element = None
        self.ref_mapping = {}

        self.id = None

        if self.__class__.__name__ not in Model.class_attribute_maps:
            attribute_map = {}
            for class_ in self.__class__.__mro__:
                if class_ == object:
                    break

                # overwrite the super class' attribute map with what we've already loaded
                try:
                    super_attribute_map = class_.ATTRIBUTE_MAP.copy()
                except AttributeError:
                    continue
                super_attribute_map.update(attribute_map)
                attribute_map = super_attribute_map
            Model.class_attribute_maps[self.__class__.__name__] = attribute_map
        self.attribute_map = Model.class_attribute_maps[self.__class__.__name__]

        if self.__class__.__name__ not in Model.class_tag_maps:
            tag_map = {}
            for class_ in self.__class__.__mro__:
                if class_ == object:
                    break

                # overwrite the super class' tag map with what we've already loaded
                try:
                    super_tag_map = class_.TAG_MAP.copy()
                except AttributeError:
                    continue
                super_tag_map.update(tag_map)
                tag_map = super_tag_map
            Model.class_tag_maps[self.__class__.__name__] = tag_map
        self.tag_map = Model.class_tag_maps[self.__class__.__name__]

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
            self.xml_namespace, self.model_namespace, self.tag_name = Model.parse_tag(el.tag)

        for attrib in self.attribute_map:
            if 'required' in self.attribute_map[attrib] and self.attribute_map[attrib]['required'] and attrib not in self.element.attrib:
                logger.critical(el.tag + ' must define ' + attrib + ' attribute')
                import sys
                sys.exit()

        for name, value in el.attrib.items():
            if not self.parse_attribute(name, value):
                logger.critical('Unknown attrib in ' + el.tag + ': ' + name + ' = ' + value)
                import sys
                sys.exit()

        sub_el_counts = {}
        for sub_el in el:
            if not self.parse_element(sub_el):
                logger.critical('Unknown element in ' + el.tag + ': ' + sub_el.tag)
                import sys
                sys.exit()
            if sub_el.tag not in sub_el_counts:
                sub_el_counts[sub_el.tag] = 1
            else:
                sub_el_counts[sub_el.tag] += 1

        for tag in self.tag_map:
            if 'minCount' in self.tag_map[tag] and (tag not in sub_el_counts or sub_el_counts[tag] < self.tag_map[tag]['minCount']):
                logger.critical(el.tag + ' does not contain a required sub element: ' + tag)
                import sys
                sys.exit()

    def parse_attribute(self, name, value):
        if name in self.attribute_map:
            if 'ignore' in self.attribute_map[name] and self.attribute_map[name]['ignore']:
                logger.debug('Ignoring attribute ' + name + ' = ' + value)
                return True

            if 'in' in self.attribute_map[name]:
                setattr(self, self.attribute_map[name]['in'], value)
                logger.debug('Set attribute ' + self.attribute_map[name]['in'] + ' = ' + value)
            else:
                xml_namespace, model_namespace, attr_name = Model.parse_tag(name)
                name = attr_name.replace('-', '_')
                setattr(self, name, value)
                logger.debug('Set attribute ' + name + ' = ' + value)
            return True
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

    def parse_element(self, el):
        xml_namespace, model_namespace, tag_name = Model.parse_tag(el.tag)
        for tag in [el.tag, tag_name]:
            # check both namespace + tag_name and just tag_name
            if tag in self.tag_map:
                if 'ignore' in self.tag_map[tag] and self.tag_map[tag]['ignore']:
                    return True

                if 'append' in self.tag_map[tag]:
                    #from scap.model.List import List
                    lst = getattr(self, self.tag_map[tag]['append'])
                    if 'type' in self.tag_map[tag]:
                        type_ = self.tag_map[tag]['type']
                        import scap.model.xs
                        if type_ in scap.model.xs:
                            lst.append(type_().parse_value(el))
                        else:
                            raise NotImplementedError('Type value ' + type_ + ' not defined in scap.model.xs')
                    else:
                        lst.append(Model.load(self, el))
                    logger.debug('Appended ' + el.tag + ' to ' + self.tag_map[tag]['append'])
                    return True

                if 'map' in self.tag_map[tag]:
                    #from scap.model.List import List
                    dic = getattr(self, self.tag_map[tag]['map'])
                    if 'key' in self.tag_map[tag]:
                        key = el.attrib[self.tag_map[tag]['key']]
                    # TODO: implement keyElement as well
                    else:
                        key = el.attrib['id']
                    dic[key] = Model.load(self, el)
                    logger.debug('Mapped ' + key + ' to ' + el.tag + ' in ' + self.tag_map[tag]['map'])
                    return True

                if 'class' in self.tag_map[tag] and self.tag_map[tag]['class'] == 'scap.model.List':
                    #from scap.model.List import List
                    if 'in' in self.tag_map[tag]:
                        lst = getattr(self, self.tag_map[tag]['in'])
                    else:
                        lst = getattr(self, tag_name.replace('-', '_'))
                    for sub_el in el:
                        lst.append(Model.load(self, sub_el))
                    return True
                elif 'class' in self.tag_map[tag] and self.tag_map[tag]['class'] == 'scap.model.Dictionary':
                    #from scap.model.List import List
                    if 'in' in self.tag_map[tag]:
                        dic = getattr(self, self.tag_map[tag]['in'])
                    else:
                        dic = getattr(self, tag_name.replace('-', '_'))
                    for sub_el in el:
                        if 'key' in self.tag_map[tag]:
                            key = sub_el.attrib[self.tag_map[tag]['key']]
                        # TODO: implement keyElement as well
                        else:
                            key = sub_el.attrib['id']
                        dic[key] = Model.load(self, sub_el)
                    return True

                if 'in' in self.tag_map[tag]:
                    setattr(self, self.tag_map[tag]['in'], Model.load(self, el))
                else:
                    name = tag_name.replace('-', '_')
                    setattr(self, name, Model.load(self, el))
                return True
        return False

    # Template
    # def parse_element(self, el):
    #     if el.tag == '{namespace}tag':
    #         self.tags.append(el.tag)
    #     else:
    #         return super(SubClass, self).parse_element(el)
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

        #logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
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
            self.xml_namespace, self.model_namespace, self.tag_name = Model.parse_tag(tag)
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
