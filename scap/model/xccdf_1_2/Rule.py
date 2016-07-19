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

from scap.model.xccdf_1_2.GroupRuleCommon import GroupRuleCommon
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Rule(GroupRuleCommon):
    def __init__(self):
        super(Rule, self).__init__()
        self.selected = False
        self.selector = None
        self.selected_check = None
        self.checks = {}

    def parse_attrib(self, name, value):
        ignore = [
            'role',
            'severity',
            'multiple',
        ]
        if name in ignore:
            return True
        else:
            return super(Rule, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        ignore = [
            '{http://checklists.nist.gov/xccdf/1.2}ident',
            '{http://checklists.nist.gov/xccdf/1.2}impact-metric',
            '{http://checklists.nist.gov/xccdf/1.2}profile-note',
            '{http://checklists.nist.gov/xccdf/1.2}fixtext',
            '{http://checklists.nist.gov/xccdf/1.2}fix',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ]
        if sub_el.tag in ignore:
            return True
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}complex-check':
            from scap.model.xccdf_1_2.ComplexCheck import ComplexCheck
            self.selected_check = ComplexCheck()
            self.selected_check.from_xml(self, sub_el)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}check':
            from scap.model.xccdf_1_2.Check import Check
            check = Check()
            check.from_xml(self, sub_el)
            if 'selector' in sub_el.attrib:
                self.checks[sub_el.attrib['selector']] = check
                if self.selected_check is None:
                    self.selected_check = check
            else:
                self.selected_check = check
        else:
            return super(Rule, self).parse_sub_el(sub_el)
        return True

    def from_xml(self, parent, el):
        super(Rule, self).from_xml(parent, el)

        if self.selected_check is None:
            logger.critical('Could not load check from rule ' + self.id)
            import sys
            sys.exit()

    def select_check(self, selector):
        self.selected_check = self.checks[selector]
