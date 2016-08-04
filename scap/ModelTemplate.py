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
class ModelTemplate(Model):
    ATTRIBUTE_MAP = {
    
    }
    TAG_MAP = {

    }

    def __init__(self):
        super(ModelTemplate, self).__init__()

    # def parse_attribute(self, name, value):
    #     if name == 'id':
    #         self.id = value
    #     else:
    #         return super(ModelTemplate, self).parse_attribute(name, value)
    #     return True

    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{namespace}tag':
    #         self.tags.append(sub_el.tag)
    #     elif sub_el.tag == '{namespace}tag':
    #         self.tag = sub_el.text
    #     elif sub_el.tag == '{namespace}flag':
    #         self.flag = self.parse_boolean(value)
    #     else:
    #         return super(ModelTemplate, self).parse_element(sub_el)
    #     return True

    # def get_attributes(self):
    #     attribs = super(Model, self).get_attributes()
    #
    #     ###
    #
    #     return attribs

    # def get_sub_elements(self):
    #     sub_els = super(Model, self).get_sub_elements()
    #
    #     ###
    #
    #     return sub_els
