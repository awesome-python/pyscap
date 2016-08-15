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
from scap.model.scap_1_2.UseCaseEnumeration import USE_CASE_ENUMERATION
from scap.model.scap_1_2.SCAPVersionEnumeration import SCAP_VERSION_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class DataStreamType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/scap/source/1.2}dictionaries': { 'class': 'RefListType' },
            '{http://scap.nist.gov/schema/scap/source/1.2}checklists': { 'class': 'RefListType' },
            '{http://scap.nist.gov/schema/scap/source/1.2}checks': { 'class': 'RefListType' },
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-components': {'ignore': True},
        },
        'attributes': {
            'id': {'required': True, 'type': 'DataStreamIDPattern'},
            'use-case': {'required': True, 'ignore': True, 'enum': USE_CASE_ENUMERATION},
            'scap-version': {'required': True, 'ignore': True, 'enum': SCAP_VERSION_ENUMERATION},
            'timestamp': {'required': True, 'ignore': True, 'type': 'DateTime'},
        },
    }
    def __init__(self):
        super(DataStreamType, self).__init__()    # {http://checklists.nist.gov/xccdf/1.2}data-stream

        self.selected_checklist = None

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
