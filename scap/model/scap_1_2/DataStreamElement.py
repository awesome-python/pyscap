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
class DataStreamElement(Model):
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/scap/source/1.2',
        'tag_name': 'data-stream',
        'elements': {
            '{http://scap.nist.gov/schema/scap/source/1.2}dictionaries': { 'class': 'RefListType', 'min': 0 },
            '{http://scap.nist.gov/schema/scap/source/1.2}checklists': { 'class': 'RefListType', 'min': 0 },
            '{http://scap.nist.gov/schema/scap/source/1.2}checks': { 'class': 'RefListType' },
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-components': {'min': 0, 'class': 'RefListType' },
        },
        'attributes': {
            'id': {'required': True, 'type': 'DataStreamIDPattern'},
            'use-case': {'required': True, 'enum': USE_CASE_ENUMERATION}, # TODO: spec also allows Token
            'scap-version': {'required': True, 'enum': SCAP_VERSION_ENUMERATION}, # TODO: spec also allows Token
            'timestamp': {'required': True, 'ignore': True, 'type': 'DateTime'},
        },
    }
