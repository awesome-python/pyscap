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
from scap.model.xccdf_1_2.CheckOperatorEnumeration import CHECK_OPERATOR_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class ComplexCheckType(Model):
    MODEL_MAP = {
        'attributes': {
            'operator': {'enum': CHECK_OPERATOR_ENUMERATION, 'required': True},
            'negate': {'type': 'Boolean', 'default': False},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}check': {'class': 'CheckType', 'append': 'checks'},
            '{http://checklists.nist.gov/xccdf/1.2}complex-check': {'class': 'ComplexCheckType', 'append': 'checks'},
        },
    }

    # def __init__(self):
    #     super(ComplexCheckType, self).__init__()
    #     self.checks = []
    #     self.negate = False
    #     self.operator = 'AND'
    #
    # def parse_attribute(self, name, value):
    #     if name == 'negate':
    #         self.negate = self.parse_boolean(value)
    #     elif name == 'operator':
    #         self.negate = value
    #     else:
    #         return super(ComplexCheckType, self).parse_attribute(name, value)
    #     return True
    #
    # def parse_element(self, sub_el):
    #     if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}complex-check' \
    #         or sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}check':
    #         self.checks.append(Model.load(self, sub_el))
    #     else:
    #         return super(ComplexCheckType, self).parse_element(sub_el)
    #     return True
