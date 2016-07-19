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

from scap.model.Simple import Simple
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Profile(Simple):
    def __init__(self):
        super(Profile, self).__init__()
        self.rules = {}
        self.values = {}

    def parse_attrib(self, name, value):
        ignore = [
        ]
        if name in ignore:
            return True
        elif name == 'extends':
            logger.critical('Profiles with @extends are not supported')
            import sys
            sys.exit()
        else:
            return super(Profile, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        ignore = [
            '{http://checklists.nist.gov/xccdf/1.2}status',
            '{http://checklists.nist.gov/xccdf/1.2}dc-status',
            '{http://checklists.nist.gov/xccdf/1.2}version',
            '{http://checklists.nist.gov/xccdf/1.2}title',
            '{http://checklists.nist.gov/xccdf/1.2}description',
            '{http://checklists.nist.gov/xccdf/1.2}reference',
            '{http://checklists.nist.gov/xccdf/1.2}platform',
            '{http://checklists.nist.gov/xccdf/1.2}metadata',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ]
        if sub_el.tag in ignore:
            return True
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}select':
            if sub_el.attrib['idref'] not in self.parent.rules:
                logger.critical('Rule idref in Profile not found: ' + sub_el.attrib['idref'])
                import sys
                sys.exit()
            r = self.parent.rules[sub_el.attrib['idref']]
            if sub_el.attrib['selected'] == 'true':
                logger.info('Rule selected by profile: ' + r.id)
                self.rules[r.id] = r
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}set-complex-value':
            logger.critical('set-complex-value is not supported')
            import sys
            sys.exit()
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}set-value':
            logger.critical('set-value is not supported')
            import sys
            sys.exit()
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}refine-value':
            if sub_el.attrib['idref'] not in self.parent.values:
                logger.critical('Value idref in Profile not found: ' + sub_el.attrib['idref'])
                import sys
                sys.exit()
            v = self.parent.values[sub_el.attrib['idref']]
            logger.info('Selecting value for ' + v.id + ' using selector ' + sub_el.attrib['selector'] + ' in profile ' + self.id)
            self.values[v.id]['value'] = v.selectors[sub_el.attrib['selector']]
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}refine-rule':
            if sub_el.attrib['idref'] not in self.parent.rules:
                logger.critical('Rule idref in Profile not found: ' + sub_el.attrib['idref'])
                import sys
                sys.exit()
            r = self.parent.rules[sub_el.attrib['idref']]
            logger.info('Selecting check ' + sub_el.attrib['selector'] + ' for rule ' + r.id)
            r.select_check(sub_el.attrib['selector'])
        else:
            return super(Profile, self).parse_sub_el(sub_el)
        return True

    def from_xml(self, parent, el):
        # copy in the rules that are selected by default
        for rule_id in parent.selected_rules:
            self.rules[rule_id] = parent.rules[rule_id]
        for v in parent.values.values():
            self.values[v.id] = { 'model': v, 'value': v.default }

        super(Profile, self).from_xml(parent, el)
