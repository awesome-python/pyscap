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
class BenchmarkType(Model):
    ATTRIBUTE_MAP = {
        'id': {'required': True},
        'Id': {'ignore': True},
        'resolved': {'ignore': True},
        'style': {'ignore': True},
        'style-href': {'ignore': True},
    }
    TAG_MAP = {
        '{http://checklists.nist.gov/xccdf/1.2}status': {'ignore': True},
        '{http://purl.org/dc/elements/1.1/}dc-status': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}title': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}description': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}notice': {'type': 'String', 'map': 'notices'},
        '{http://checklists.nist.gov/xccdf/1.2}front-matter': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}rear-matter': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}reference': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}plain-text': {'ignore': True},
        '{http://cpe.mitre.org/language/2.0}platform-specification': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}platform': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}version': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}metadata': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}model': {'ignore': True},
        '{http://checklists.nist.gov/xccdf/1.2}Profile': {'class': 'ProfileType', 'map': 'profiles'},
        '{http://checklists.nist.gov/xccdf/1.2}Value': {'class': 'ValueType', 'map': 'values'},
        '{http://checklists.nist.gov/xccdf/1.2}Group': {'class': 'GroupType', 'map': 'groups'},
        '{http://checklists.nist.gov/xccdf/1.2}Rule': {'class': 'RuleType', 'map': 'rules'},
        '{http://checklists.nist.gov/xccdf/1.2}TestResult': {'class': 'TestResultType', 'map': 'tests'},
        '{http://checklists.nist.gov/xccdf/1.2}signature': {'ignore': True},
    }

    def __init__(self):
        super(BenchmarkType, self).__init__()

        self.notices = {}
        self.rules = {}
        self.values = {}
        self.profiles = {}
        self.groups = {}
        self.test_results = {}
        self.selected_rules = []

    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}notice':
    #         logger.info('Notice: \n' + sub_el.text)
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Profile':
    #         from scap.model.xccdf_1_2.ProfileType import ProfileType
    #         logger.debug('found profile ' + sub_el.attrib['id'])
    #         p = ProfileType()
    #         # save the sub_el for later so that profiles parse after rules, values
    #         self.profile_elements[sub_el.attrib['id']] = sub_el
    #         self.profiles[sub_el.attrib['id']] = p
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Value':
    #         self.values[sub_el.attrib['id']] = Model.load(self, sub_el)
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Group':
    #         g = Model.load(self, sub_el)
    #         self.rules.update(g.get_rules())
    #         self.values.update(g.get_values())
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Rule':
    #         r = Model.load(self, sub_el)
    #         self.rules[sub_el.attrib['id']] = r
    #         if r.selected:
    #             self.selected_rules.append(r.id)
    #     elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}TestResult':
    #         self.test_results[sub_el.attrib['id']] = Model.load(self, sub_el)
    #     else:
    #         return super(BenchmarkType, self).parse_element(sub_el)
    #     return True
    #
    def from_xml(self, parent, el):
        super(BenchmarkType, self).from_xml(parent, el)

        for notice in self.notices.values():
            logger.info('Notice: \n' + notice)

        for profile_id in self.profiles:
            logger.debug('found profile ' + profile_id)
