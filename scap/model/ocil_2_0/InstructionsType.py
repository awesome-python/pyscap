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
class InstructionsType(object):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}step': {'class': 'StepType'},
        }
    }
    def __init__(self):
        super(InstructionsType, self).__init__()

        self.title = None
        self.steps = []

        # self.required_attributes.extend([
        # ])
        # self.ignore_attributes.extend([
        # ])
        # self.required_sub_elements.extend([
        # ])
        # self.ignore_sub_elements.extend([
        # ])

    # def parse_attribute(self, name, value):
    #     if name == 'id':
    #         self.id = value
    #     else:
    #         return super(ModelTemplate, self).parse_attribute(name, value)
    #     return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}title':
            self.title = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}step':
            self.steps.append(Model.load(self, sub_el))
        else:
            return super(InstructionsType, self).parse_element(sub_el)
        return True

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
