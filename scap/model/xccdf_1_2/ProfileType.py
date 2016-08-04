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
class ProfileType(Model):
    def __init__(self):
        super(ProfileType, self).__init__()
        self.selected_rules = []
        self.rule_check_selections = {}
        self.value_selections = {}

        self.ignore_attributes.extend(['selected', 'weight'])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}version',
            '{http://checklists.nist.gov/xccdf/1.2}title',
            '{http://checklists.nist.gov/xccdf/1.2}description',
            '{http://checklists.nist.gov/xccdf/1.2}reference',
            '{http://checklists.nist.gov/xccdf/1.2}platform',
            '{http://checklists.nist.gov/xccdf/1.2}metadata',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_attribute(self, name, value):
        if name == 'extends':
            logger.critical('Profiles with @extends are not supported')
            import sys
            sys.exit()
        else:
            return super(ProfileType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}select':
            if sub_el.attrib['idref'] not in self.parent.rules:
                logger.critical('Rule idref in Profile not found: ' + sub_el.attrib['idref'])
                import sys
                sys.exit()
            r = self.parent.rules[sub_el.attrib['idref']]
            if sub_el.attrib['selected'] == 'true':
                logger.debug('Rule ' + sub_el.attrib['idref'] + ' selected by profile ' + self.id)
                self.selected_rules.append(sub_el.attrib['idref'])

                if sub_el.attrib['idref'] not in self.rule_check_selections:
                    self.rule_check_selections[sub_el.attrib['idref']] = None
            else:
                try:
                    logger.debug('Rule ' + sub_el.attrib['idref'] + ' un-selected by profile ' + self.id)
                    self.selected_rules.remove(sub_el.attrib['idref'])
                except KeyError:
                    logger.warning('Rule ' + sub_el.attrib['idref'] + ' was not previously selected by profile ' + self.id)
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
            if sub_el.attrib['selector'] not in v.selectors:
                logger.critical('Selector in Value not found: ' + sub_el.attrib['selector'])
                import sys
                sys.exit()
            logger.info('Using selector ' + sub_el.attrib['selector'] + ' for value ' + v.id + ' in profile ' + self.id)
            self.value_selections[v.id] = sub_el.attrib['selector']
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}refine-rule':
            if sub_el.attrib['idref'] not in self.parent.rules:
                logger.critical('Rule idref in Profile not found: ' + sub_el.attrib['idref'])
                import sys
                sys.exit()
            logger.info('Using check selector ' + sub_el.attrib['selector'] + ' for rule ' + sub_el.attrib['idref'] + ' in profile ' + self.id)
            self.rule_check_selections[sub_el.attrib['idref']] = sub_el.attrib['selector']
        else:
            return super(ProfileType, self).parse_element(sub_el)
        return True

    def from_xml(self, parent, el):
        # copy in the rules that are selected by default
        for rule_id in parent.selected_rules:
            self.selected_rules[rule_id] = parent.rules[rule_id]

        super(ProfileType, self).from_xml(parent, el)
