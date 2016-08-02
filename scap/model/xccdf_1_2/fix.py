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
class fix(Model):
    def __init__(self):
        super(fix, self).__init__()

        self.ignore_attributes.extend([
            'fixref',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}ident',
            '{http://checklists.nist.gov/xccdf/1.2}impact-metric',
            '{http://checklists.nist.gov/xccdf/1.2}profile-note',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_sub_el(self, sub_el):
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
            return super(fix, self).parse_sub_el(sub_el)
        return True
