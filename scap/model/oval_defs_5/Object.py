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
class Object(Model):
    @staticmethod
    def load(parent, obj_el):
        from scap.model.oval_defs_5_windows.RegistryObject import RegistryObject
        from scap.model.oval_defs_5_windows.WUAUpdateSearcherObject import WUAUpdateSearcherObject
        obj_map = {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_object': RegistryObject,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_object': WUAUpdateSearcherObject,
        }
        if obj_el.tag not in obj_map:
            logger.critical('Unknown obj tag: ' + obj_el.tag)
            import sys
            sys.exit()
        obj = obj_map[obj_el.tag]()
        obj.from_xml(parent, obj_el)
        return obj

    # abstract
    def __init__(self, tag_name=None):
        super(Object, self).__init__(tag_name)

        self.set = None
        self.filter = None

        self.ignore_attributes.extend([
            'version',
            'comment',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated object ' + self.id)
        else:
            return super(Object, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}set':
            from scap.model.oval_defs_5.Set import Set
            s = Set()
            s.from_xml(self, sub_el)
            self.set = s
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}filter':
            from scap.model.oval_defs_5.Filter import Filter
            f = Filter()
            f.from_xml(self, sub_el)
            self.filter = f
        else:
            return super(Object, self).parse_sub_el(sub_el)
        return True
