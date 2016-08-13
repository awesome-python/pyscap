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
from scap.model import NAMESPACES

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
class Model(object):
    MODEL_MAP = {
        'attributes': {
            '{http://www.w3.org/XML/1998/namespace}lang': {'ignore': True},
            '{http://www.w3.org/XML/1998/namespace}base': {'ignore': True},
            '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': {'ignore': True},
        },
    }

    model_maps = {}

    @staticmethod
    def parse_tag(tag):
        # parse tag
        if tag[0] == '{':
            xml_namespace, tag_name = tag[1:].split('}')
        else:
            return None, tag

        if xml_namespace not in NAMESPACES:
            logger.critical('Unsupported ' + tag_name + ' tag with namespace: ' + xml_namespace)
            import sys
            sys.exit()

        return xml_namespace, tag_name

    @staticmethod
    def load(parent, child_el):
        xml_namespace, tag_name = Model.parse_tag(child_el.tag)

        if xml_namespace not in NAMESPACES:
            raise NotImplementedError('Namespace ' + xml_namespace + ' is not supported')
        model_namespace = NAMESPACES[xml_namespace]

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
                mmap = parent.__class__.MODEL_MAP
            except AttributeError:
                sys.exit(parent.__class__.__name__ + ' does not define MODEL_MAP')
            try:
                elmap = mmap['elements']
            except KeyError:
                sys.exit(parent.__class__.__name__ + ' does not define mapping for elements')
            try:
                module_name = elmap[child_el.tag]['class']
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
        inst.from_xml(parent, child_el)

        return inst

    @staticmethod
    def load_item(parent, child_el, classes):
        xml_namespace, tag_name = Model.parse_tag(child_el.tag)

        if xml_namespace not in NAMESPACES:
            raise NotImplementedError('Namespace ' + xml_namespace + ' is not supported')
        model_namespace = NAMESPACES[xml_namespace]

        # try to load the tag's module
        import sys, importlib
        if child_el.tag in classes:
            module_name = classes[child_el.tag]
        elif '{' + xml_namespace + '}*' in classes:
            module_name = classes['{' + xml_namespace + '}*']
        elif '*' in classes:
            module_name = classes['*']
        else:
            raise NotImplementedError('Item tag ' + child_el.tag + ' is not mapped to a class by ' + parent.__class__.__name__)

        if module_name is None:
            return None

        model_module = 'scap.model.' + model_namespace + '.' + module_name
        if model_module not in sys.modules:
            logger.debug('Loading module ' + model_module)

            mod = importlib.import_module(model_module)
        else:
            mod = sys.modules[model_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, module_name)
        inst = class_()
        inst.from_xml(parent, child_el)

        return inst

    def __init__(self):
        self.parent = None
        self.element = None
        self.ref_mapping = {}

        if self.__class__.__name__ not in Model.model_maps:
            at_map = {}
            el_map = {}
            xml_namespace = None
            tag_name = None
            for class_ in self.__class__.__mro__:
                if class_ == object:
                    break

                try:
                    class_.MODEL_MAP
                except AttributeError:
                    logger.critical('Class ' + class_.__name__ + ' does not define MODEL_MAP')
                    import sys
                    sys.exit()

                # overwrite the super class' ns & tag with what we've already loaded
                try:
                    xml_namespace = class_.MODEL_MAP['xml_namespace']
                except KeyError:
                    logger.debug('Class ' + class_.__name__ + ' does not have MODEL_MAP[xml_namespace] defined')
                try:
                    tag_name = class_.MODEL_MAP['tag_name']
                except KeyError:
                    logger.debug('Class ' + class_.__name__ + ' does not have MODEL_MAP[tag_name] defined')

                # overwrite the super class' attribute map with what we've already loaded
                try:
                    super_atmap = class_.MODEL_MAP['attributes'].copy()
                    super_atmap.update(at_map)
                    at_map = super_atmap
                except KeyError:
                    logger.debug('Class ' + class_.__name__ + ' does not have MODEL_MAP[attributes] defined')

                # overwrite the super class' element map with what we've already loaded
                try:
                    super_elmap = class_.MODEL_MAP['elements'].copy()
                    super_elmap.update(el_map)
                    el_map = super_elmap
                except KeyError:
                    logger.debug('Class ' + class_.__name__ + ' does not have MODEL_MAP[elements] defined')

            Model.model_maps[self.__class__.__name__] = {
                'xml_namespace': xml_namespace,
                'tag_name': tag_name,
                'attributes': at_map,
                'elements': el_map,
            }
        self.model_map = Model.model_maps[self.__class__.__name__]

        if 'xml_namespace' in self.model_map:
            if self.model_map['xml_namespace'] not in NAMESPACES:
                raise ValueError('Unknown namespace: ' + self.model_map['xml_namespace'])
        if 'tag_name' in self.model_map:
            self.tag_name = self.model_map['tag_name']

        # set default values
        for name in self.model_map['attributes']:
            attr_map = self.model_map['attributes'][name]
            if 'default' in attr_map:
                value = attr_map['default']
                if 'in' in attr_map:
                    setattr(self, attr_map['in'], value)
                    logger.debug('Default of attribute ' + attr_map['in'] + ' = ' + str(value))
                else:
                    xml_namespace, attr_name = Model.parse_tag(name)
                    name = attr_name.replace('-', '_')
                    setattr(self, name, value)
                    logger.debug('Default of attribute ' + name + ' = ' + str(value))

        # initialize structures
        for t in self.model_map['elements']:
            xml_namespace, tag_name = Model.parse_tag(t)
            for tag in [t, tag_name]:
                if tag in self.model_map['elements']:
                    tag_map = self.model_map['elements'][tag]
                    if 'append' in tag_map:
                        # initialze the array if it doesn't exist
                        if tag_map['append'] not in self.__dict__.keys():
                            setattr(self, tag_map['append'], [])
                    elif 'map' in tag_map:
                        # initialze the dict if it doesn't exist
                        if tag_map['map'] not in self.__dict__.keys():
                            setattr(self, tag_map['map'], {})
                    elif 'dictionary' in tag_map:
                        dict_name = tag_map['dictionary']

                        # initialze the dict if it doesn't exist
                        if dict_name not in self.__dict__.keys():
                            setattr(self, dict_name, {})

    def get_tag_name(self):
        if 'tag_name' not in self.model_map:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag_name')
        return self.model_map['tag_name']

    def get_xml_namespace(self):
        if 'xml_namespace' not in self.model_map:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define namespace')
        return self.model_map['xml_namespace']

    def get_model_namespace(self):
        xml_namespace = self.get_xml_namespace()
        if xml_namespace not in NAMESPACES:
            raise NotImplementedError('Namespace ' + xml_namespace + ' is not supported')
        return NAMESPACES[xml_namespace]

    def get_tag(self):
        return '{' + self.get_xml_namespace() + '}' + self.get_tag_name()

    def from_xml(self, parent, el):
        self.parent = parent
        self.element = el

        logger.debug('Parsing ' + el.tag + ' element into ' + self.__class__.__name__ + ' class')

        for attrib in self.model_map['attributes']:
            if 'required' in self.model_map['attributes'][attrib] and self.model_map['attributes'][attrib]['required'] and attrib not in self.element.attrib:
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

        for tag in self.model_map['elements']:
            tag_map = self.model_map['elements'][tag]
            if 'minCount' in tag_map and (tag not in sub_el_counts or sub_el_counts[tag] < tag_map['minCount']):
                logger.critical(el.tag + ' does not contain a required sub element: ' + tag)
                import sys
                sys.exit()

    def _parse_value_as_type(self, value, type_):
        import importlib
        if '.' in type_:
            try:
                mod = importlib.import_module('scap.model.' + type_)
            except ImportError:
                raise NotImplementedError('Type value scap.model.' + type_ + ' was not found')
        else:
            try:
                mod = importlib.import_module('scap.model.xs.' + type_)
            except ImportError:
                model_namespace = self.get_model_namespace()
                try:
                    mod = importlib.import_module('scap.model.' + model_namespace + '.' + type_)
                except ImportError:
                    raise NotImplementedError('Type value ' + type_ + ' not defined in scap.model.xs or local namespace (scap.model.' + model_namespace + ')')
        class_ = getattr(mod, type_)
        return class_().parse_value(value)

    def parse_attribute(self, name, value):
        xml_namespace, attr_name = Model.parse_tag(name)
        if xml_namespace is None:
            ns_any = '{' + self.model_map['xml_namespace'] + '}*'
        else:
            ns_any = '{' + xml_namespace + '}*'
        for name in [name, attr_name, ns_any, '*']:
            attr_map = self.model_map['attributes'][name]
            if name in self.model_map['attributes']:
                if 'ignore' in attr_map and attr_map['ignore']:
                    logger.debug('Ignoring attribute ' + name + ' = ' + value)
                    return True

                if 'notImplemented' in attr_map and attr_map['notImplemented']:
                    raise NotImplementedError(name + ' attribute support is not implemented')

                if 'enum' in attr_map and value not in attr_map['enum']:
                    raise ValueError(name + ' attribute must be one of ' + str(attr_map['enum']))

                # convert value
                if 'type' in attr_map:
                    logger.debug('Parsing ' + str(value) + ' as ' + attr_map['type'] + ' type')
                    value = self._parse_value_as_type(value, attr_map['type'])

                if 'in' in attr_map:
                    setattr(self, attr_map['in'], value)
                    logger.debug('Set attribute ' + attr_map['in'] + ' = ' + str(value))
                else:
                    name = attr_name.replace('-', '_')
                    setattr(self, name, value)
                    logger.debug('Set attribute ' + name + ' = ' + str(value))
                return True
        return False

    def parse_element(self, el):
        xml_namespace, tag_name = Model.parse_tag(el.tag)
        if xml_namespace is None:
            ns_any = '{' + self.model_map['xml_namespace'] + '}*'
        else:
            ns_any = '{' + xml_namespace + '}*'
        for tag in [el.tag, tag_name, ns_any, '*']:
            # check both namespace + tag_name and just tag_name
            if tag in self.model_map['elements']:
                tag_map = self.model_map['elements'][tag]
                if 'ignore' in tag_map and tag_map['ignore']:
                    return True

                if 'notImplemented' in tag_map and tag_map['notImplemented']:
                    raise NotImplementedError(tag + ' element support is not implemented')

                if 'append' in tag_map:
                    lst = getattr(self, tag_map['append'])
                    if 'type' in tag_map:
                        value = self._parse_value_as_type(el.text, tag_map['type'])
                        lst.append(value)
                        logger.debug('Appended "' + value + '" to ' + tag_map['append'])
                    else:
                        lst.append(Model.load(self, el))
                        logger.debug('Appended ' + el.tag + ' to ' + tag_map['append'])
                elif 'map' in tag_map:
                    dic = getattr(self, tag_map['map'])
                    if 'key' in tag_map:
                        try:
                            key = el.attrib[tag_map['key']]
                        except KeyError:
                            key = None
                    # TODO: implement keyElement as well
                    else:
                        key = el.attrib['id']

                    if 'value' in tag_map:
                        try:
                            value = el.attrib[tag_map['value']]
                            if 'type' in tag_map:
                                value = self._parse_value_as_type(value, tag_map['type'])
                        except KeyError:
                            value = None
                        dic[key] = value
                        logger.debug('Mapped ' + str(key) + ' to ' + str(value) + ' in ' + tag_map['map'])
                    # TODO: implement valueElement? as well
                    else:
                        if 'type' in tag_map:
                            value = self._parse_value_as_type(el.text, tag_map['type'])
                            dic[key] = value
                            logger.debug('Mapped ' + str(key) + ' to ' + str(value) + ' in ' + tag_map['map'])
                        else:
                            dic[key] = Model.load(self, el)
                            logger.debug('Mapped ' + str(key) + ' to ' + el.tag + ' in ' + tag_map['map'])
                elif 'dictionary' in tag_map:
                    dict_name = tag_map['dictionary']
                    dic = getattr(self, dict_name)
                    if 'classes' not in tag_map:
                        raise NotImplementedError('List tag ' + tag + ' does not define classes')
                    for sub_el in el:
                        if 'key' in tag_map:
                            key = sub_el.attrib[tag_map['key']]
                        # TODO: implement keyElement as well
                        else:
                            key = sub_el.attrib['id']
                        item = Model.load_item(self, sub_el, tag_map['classes'])
                        if item is not None:
                            dic[key] = item
                elif 'class' in tag_map:
                    if 'in' in tag_map:
                        name = tag_map['in']
                        setattr(self, name, Model.load(self, el))
                    else:
                        name = tag_name.replace('-', '_')
                        setattr(self, name, Model.load(self, el))
                elif 'type' in tag_map:
                    value = self._parse_value_as_type(el.text, tag_map['type'])
                    if 'in' in tag_map:
                        name = tag_map['in']
                        setattr(self, name, value)
                    else:
                        name = tag_name.replace('-', '_')
                        setattr(self, name, value)
                elif 'enum' in tag_map:
                    if el.text not in tag_map['enum']:
                        raise ValueError(tag + ' value must be one of ' + str(tag_map['enum']))
                    if 'in' in tag_map:
                        name = tag_map['in']
                        setattr(self, name, value)
                    else:
                        name = tag_name.replace('-', '_')
                        setattr(self, name, value)
                else:
                    return False
                return True
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

    def produce_attribute(self, name):
        if name.endswith('*'):
            return None

        xml_namespace, attr_name = Model.parse_tag(name)
        attr_map = self.model_map['attributes'][name]
        if 'in' in attr_map:
            attr_name = attr_map['in']
        else:
            attr_name = attr_name.replace('-', '_')

        try:
            value = getattr(self, attr_name)
        except AttributeError:
            if 'required' in attr_map and attr_map['required']:
                logger.critical(self.__class__.__name__ + ' must assign required attribute ' + attrib)
                import sys
                sys.exit()
            else:
                logger.debug('Skipping attribute ' + name)
                return None

        logger.debug('Setting attribute ' + name + ' to ' + value)
        return value

    def produce_sub_elements(self, tag):
        sub_els = []
        if tag.endswith('*'):
            return []

        tag_map = self.model_map['elements'][tag]
        if 'append' in tag_map:
            lst = getattr(self, tag_map['append'])
            for i in lst:
                logger.debug('Creating ' + tag + ' for value ' + i)
                el = ET.Element(tag)
                el.text = i
                sub_els.append(el)
        elif 'map' in tag_map:
            dic = getattr(self, tag_map['map'])
            if 'key' in tag_map:
                key_name = tag_map['key']
            else:
                key_name = 'id'
            for k,v in dic.items():
                el = ET.Element(tag)
                el.attrib[key_name] = k

                if 'value' in tag_map:
                    value_name = tag_map['value']
                    el.attrib[value_name] = v
                else:
                    el.text = v
                sub_els.append(el)
        elif 'dictionary' in tag_map:
            dict_name = tag_map['dictionary']
            dic = getattr(self, dict_name)
            el = ET.Element(tag)
            for k,v in dic.items():
                el.append(v.to_xml())
            sub_els.append(el)
        elif 'class' in tag_map:
            if 'in' in tag_map:
                name = tag_map['in']
            else:
                name = tag_name.replace('-', '_')
            sub_els.append(getattr(self, name).to_xml())
        elif 'type' in tag_map \
            or 'enum' in tag_map:
            if 'in' in tag_map:
                name = tag_map['in']
            else:
                name = tag_name.replace('-', '_')
            el = ET.Element(tag)
            el.text = getattr(self, name)
            sub_els.append(el)
        elif 'required' in tag_map and tag_map['required']:
            logger.critical(self.__class__.__name__ + ' must use the required element ' + tag)
            import sys
            sys.exit()
        return sub_els

    def to_xml(self):
        if self.element is None:
            self.element = ET.Element(self.get_tag())

            for name in self.model_map['attributes']:
                value = self.produce_attribute(name)
                if value is not None:
                    self.element.attrib[name] = value

            for tag in self.model_map['elements']:
                self.element.extend(self.produce_sub_elements(tag))

        return self.element
