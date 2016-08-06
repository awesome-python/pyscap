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
class TailoringType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'type': 'TailoringIDPattern', 'required': True},
            'Id': {'type': 'ID'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}benchmark': {'class': 'TailoringBenchmarkReferenceType'},
            '{http://checklists.nist.gov/xccdf/1.2}status': {'class': 'StatusType', 'append': 'statuses'},
            '{http://checklists.nist.gov/xccdf/1.2}dc-status': {'class': 'DCStatusType', 'append': 'dc_statuses'},
            '{http://checklists.nist.gov/xccdf/1.2}version': {'class': 'TailoringVersionType'},
            '{http://checklists.nist.gov/xccdf/1.2}metadata': {'class': 'MetadataType', 'append': 'metadata'},
            '{http://checklists.nist.gov/xccdf/1.2}Profile': {'class': 'ProfileType', 'append': 'profiles'},
            '{http://checklists.nist.gov/xccdf/1.2}signature': {'ignore': True, 'class': 'SignatureType'},
        },
    }
