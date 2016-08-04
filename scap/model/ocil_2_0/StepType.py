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
class StepType(object):
    TAG_MAP = {
        '{http://scap.nist.gov/schema/ocil/2.0}reference': {'class': 'ReferenceType'},
        '{http://scap.nist.gov/schema/ocil/2.0}step': {'class': 'StepType'},
    }
    def __init__(self):
        super(StepType, self).__init__()

        self.is_done = False
        self.is_required = True

        self.description = None
        self.references = []
        self.steps = []

        # self.required_attributes.extend([
        # ])
        # self.ignore_attributes.extend([
        # ])
        # self.required_sub_elements.extend([
        # ])
        # self.ignore_sub_elements.extend([
        # ])

    def parse_attribute(self, name, value):
        if name == 'is_done':
            self.is_done = self.parse_boolean(value)
        elif name == 'is_required':
            self.is_required = self.parse_boolean(value)
        else:
            return super(StepType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}description':
            self.description = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}reference':
            self.references.append(Model.load(self, sub_el))
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}step':
            self.steps.append(Model.load(self, sub_el))
        else:
            return super(StepType, self).parse_element(sub_el)
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
