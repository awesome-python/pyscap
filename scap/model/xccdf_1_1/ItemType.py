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
class ItemType(Model):
    MODEL_MAP = {
        'attributes': {
            'abstract': {'ignore': True, 'type': 'Boolean', 'default': False},
            'cluster-id': {'ignore': True, 'type': 'NCName'},
            'extends': {'ignore': True, 'type': 'NCName'},
            'hidden': {'ignore': True, 'type': 'Boolean', 'default': False},
            'prohibitChanges': {'ignore': True, 'type': 'Boolean', 'default': False},
            'Id': {'ignore': True, 'type': 'ID'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}status': {'class': 'StatusType', 'append': 'statuses', 'ignore': True, 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}dc-status': {'class': 'DCStatusType', 'append': 'dc_statuses', 'ignore': True, 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}version': {'class': 'VersionType', 'min': 0, 'max': 1, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}title': {'append': 'titles', 'class': 'TextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}description': {'append': 'descriptions', 'min': 0, 'max': None, 'class': 'HTMLTextWithSubType', 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}warning': {'class': 'WarningType', 'min': 0, 'max': None, 'type': 'String', 'append': 'warnings'},
            '{http://checklists.nist.gov/xccdf/1.1}question': {'append': 'questions', 'class': 'TextType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}reference': {'append': 'references', 'min': 0, 'max': None, 'class': 'ReferenceType', 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}metadata': {'append': 'metadata', 'min': 0, 'max': None, 'class': 'MetadataType', 'ignore': True},
        },
    }
    # abstract
    # def __init__(self):
    #     super(ItemType, self).__init__()
    #
    #     self.warnings = []
    #
    def from_xml(self, parent, el):
        super(ItemType, self).from_xml(parent, el)

        for warning in self.warnings:
            logger.warning('Warning:\n' + warning)
