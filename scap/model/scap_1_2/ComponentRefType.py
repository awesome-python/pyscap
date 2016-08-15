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
class ComponentRefType(Model):
    MODEL_MAP = {
        'elements': {
            '{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog': {'class': 'Catalog'},
        },
        'attributes': {
            'id': {'required': True, 'type': 'ComponentRefIDPattern'},
            '{http://www.w3.org/1999/xlink}type': {'enum': ['simple'], 'ignore': True},
            '{http://www.w3.org/1999/xlink}href': {'type': 'String', 'required': True},
        },
    }
    # def __init__(self):
    #     super(ComponentRefType, self).__init__()    # {http://checklists.nist.gov/xccdf/1.2}component-ref
    #
    #     self.href = None

    # def parse_attribute(self, name, value):
    #     if name == '{http://www.w3.org/1999/xlink}href':
    #         self.href = value
    #     else:
    #         return super(ComponentRefType, self).parse_attribute(name, value)
    #     return True
    #
    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog':
    #         logger.debug('Loading catalog for ' + self.href)
    #         from scap.model.xml_cat_1_1.Catalog import Catalog
    #         cat = Catalog()
    #         cat.from_xml(self, sub_el)
    #         self.set_ref_mapping(cat.to_dict())
    #     else:
    #         return super(ComponentRefType, self).parse_element(sub_el)
    #     return True
    #
    def from_xml(self, parent, sub_el):
        super(ComponentRefType, self).from_xml(parent, sub_el)

        try:
            self.set_ref_mapping(self.catalog.to_dict())
        except AttributeError:
            pass

    def resolve(self):
        component = self.resolve_reference(self.href)
        comp = component.model
        comp.set_ref_mapping(self.ref_mapping)
        return comp
