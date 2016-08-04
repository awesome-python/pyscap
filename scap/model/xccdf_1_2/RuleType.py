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

from scap.model.xccdf_1_2.SelectableItemType import SelectableItemType
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class RuleType(SelectableItemType):
    TAG_MAP = {
        '{http://checklists.nist.gov/xccdf/1.2}complex-check': {'class': 'ComplexCheckType'},
        '{http://checklists.nist.gov/xccdf/1.2}check': {'class': 'CheckType'},
        '{http://checklists.nist.gov/xccdf/1.2}fix': {'class': 'FixType'},
        '{http://checklists.nist.gov/xccdf/1.2}fixtext': {'class': 'FixtextType'},
    }

    def __init__(self):
        super(RuleType, self).__init__()

        self.multiple = False

        self.checks = {}
        self.fixes = []
        self.fixtexts = []

        self.required_attributes.append('id')
        self.ignore_attributes.extend([
            'role',
            'severity',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}ident',
            '{http://checklists.nist.gov/xccdf/1.2}impact-metric',
            '{http://checklists.nist.gov/xccdf/1.2}profile-note',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_attribute(self, name, value):
        if name == 'multiple':
            self.multiple = self.parse_boolean(value)
        else:
            return super(RuleType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}complex-check':
            self.checks[None] = Model.load(self, sub_el)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}check':
            check = Model.load(self, sub_el)
            if 'selector' in sub_el.attrib:
                self.checks[sub_el.attrib['selector']] = check
            else:
                self.checks[None] = check
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}fix':
            self.fixes.append(Model.load(self, sub_el))
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}fixtext':
            self.fixtexts.append(Model.load(self, sub_el))
        else:
            return super(RuleType, self).parse_element(sub_el)
        return True
