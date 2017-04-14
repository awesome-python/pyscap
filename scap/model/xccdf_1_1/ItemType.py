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

from scap.model.xccdf_1_1.Extendable import Extendable
import logging

logger = logging.getLogger(__name__)
class ItemType(Extendable):
    MODEL_MAP = {
        # abstract
        'attributes': {
            'abstract': {'type': 'Boolean', 'default': False},
            'cluster-id': {'ignore': True, 'type': 'NCName'},
            'extends': {'type': 'NCName'},
            'hidden': {'type': 'Boolean', 'default': False},
            'prohibitChanges': {'type': 'Boolean', 'default': False},
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

    def get_extended(self, benchmark):
        try:
            extended = benchmark.item[self.extends]
        except AttributeError:
            # If any Item’s extends property identifier does not match the
            # identifier of a visible Item of the same type, then Loading fails.
            raise ValueError('Item ' + self.id + ' unable to extend unknown item id: ' + self.extends)

        if self.hidden:
            raise ValueError('Item ' + self.id + ' unable to extend hidden item id: ' + self.extends)

        return extended

    def process(self, benchmark, host):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
