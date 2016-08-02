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
class results(Model):
    def __init__(self):
        super(results, self).__init__()

        self.start_time = None
        self.end_time = None

        self.title = None
        self.questionnaire_results = []
        self.test_action_results = []
        self.question_results = []
        self.artifact_results = []
        self.targets = []

    def parse_attribute(self, name, value):
        if name == 'start_time':
            self.start_time = value
        elif name == 'end_time':
            self.end_time = value
        else:
            return super(results, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}title':
            self.title = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}questionnaire_results':
            for sub_sub_el in sub_el:
                self.questionnaire_results[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}test_action_results':
            for sub_sub_el in sub_el:
                self.test_action_results[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}question_results':
            for sub_sub_el in sub_el:
                self.question_results[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}artifact_results':
            for sub_sub_el in sub_el:
                self.artifact_results[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}targets':
            for sub_sub_el in sub_el:
                self.targets[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        else:
            return super(results, self).parse_sub_el(sub_el)
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
