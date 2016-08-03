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
class DataStreamType(Model):
    TAG_MAP = {
        '{http://scap.nist.gov/schema/scap/source/1.2}component-ref': {'class': 'ComponentReferenceType'},
    }
    def __init__(self):
        super(DataStreamType, self).__init__()    # {http://checklists.nist.gov/xccdf/1.2}data-stream

        self.dictionaries = {}
        self.checklists = {}
        self.checks = {}
        self.selected_checklist = None

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
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-components',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}dictionaries':
            for comp_ref_el in sub_el:
                if comp_ref_el.tag != '{http://scap.nist.gov/schema/scap/source/1.2}component-ref':
                    logger.critical(sub_el.tag + ' element can only contain component-ref elements')
                    import sys
                    sys.exit()
                comp_ref = Model.load(self, comp_ref_el)
                self.dictionaries[comp_ref.id] = comp_ref
        elif sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}checklists':
            for comp_ref_el in sub_el:
                if comp_ref_el.tag != '{http://scap.nist.gov/schema/scap/source/1.2}component-ref':
                    logger.critical(sub_el.tag + ' element can only contain component-ref elements')
                    import sys
                    sys.exit()
                comp_ref = Model.load(self, comp_ref_el)
                self.checklists[comp_ref.id] = comp_ref
        elif sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}checks':
            for comp_ref_el in sub_el:
                if comp_ref_el.tag != '{http://scap.nist.gov/schema/scap/source/1.2}component-ref':
                    logger.critical(sub_el.tag + ' element can only contain component-ref elements')
                    import sys
                    sys.exit()
                comp_ref = Model.load(self, comp_ref_el)
                self.checks[comp_ref.id] = comp_ref
        else:
            return super(DataStreamType, self).parse_sub_el(sub_el)
        return True

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            ref = self.ref_mapping[ref]

        if ref[0] == '#':
            ref = ref[1:]
            if ref in self.dictionaries:
                logger.debug('Resolving ' + ref + ' as component reference to ' + self.dictionaries[ref].href)
                return self.dictionaries[ref].resolve()
            elif ref in self.checklists:
                logger.debug('Resolving ' + ref + ' as component reference to ' + self.checklists[ref].href)
                return self.checklists[ref].resolve()
            elif ref in self.checks:
                logger.debug('Resolving ' + ref + ' as component reference to ' + self.checks[ref].href)
                return self.checks[ref].resolve()
            else:
                logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
                return self.parent.resolve_reference('#' + ref)
        else:
            logger.critical('only local references are supported: ' + ref)
            import sys
            sys.exit()
