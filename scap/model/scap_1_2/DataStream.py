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
class DataStream(Model):
    def __init__(self):
        super(DataStream, self).__init__('{http://checklists.nist.gov/xccdf/1.2}data-stream')

        self.checklists = {}
        self.checks = []

        self.required_attributes.extend([
            'id',
            'use-case',
            'scap-version',
            'timestamp',
        ])
        self.ignore_attributes.extend([
            'use-case',
            'scap-version',
            'timestamp',
        ])
        self.ignore_sub_elements.extend([
            '{http://scap.nist.gov/schema/scap/source/1.2}dictionaries',
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-components',
        ])

    def parse_sub_el(self, sub_el):
        from scap.model.scap_1_2.ComponentRef import ComponentRef
        if sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}checklists':
            for comp_ref_el in sub_el:
                if comp_ref_el.tag != '{http://scap.nist.gov/schema/scap/source/1.2}component-ref':
                    logger.critical(sub_el.tag + ' element can only contain component-ref elements')
                    import sys
                    sys.exit()
                comp_ref = ComponentRef()
                comp_ref.from_xml(self, comp_ref_el)
                self.checklists[comp_ref.id] = comp_ref
        elif sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}checks':
            for comp_ref_el in sub_el:
                if comp_ref_el.tag != '{http://scap.nist.gov/schema/scap/source/1.2}component-ref':
                    logger.critical(sub_el.tag + ' element can only contain component-ref elements')
                    import sys
                    sys.exit()
                comp_ref = ComponentRef()
                comp_ref.from_xml(self, comp_ref_el)
                self.checks.append(comp_ref)
        else:
            return super(DataStream, self).parse_sub_el(sub_el)
        return True
