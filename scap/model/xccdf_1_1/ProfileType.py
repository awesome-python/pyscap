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
class ProfileType(Extendable):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'ProfileIDPattern'},
            'prohibitChanges': {'ignore': True, 'type': 'Boolean', 'default': False},
            'abstract': {'type': 'Boolean', 'default': False},
            'note-tag': {'ignore': True, 'type': 'NCName'},
            'extends': {'type': 'NCName'},
            'Id': {'ignore': True, 'type': 'ID'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}status': {'ignore': True, 'class': 'StatusType', 'append': 'statuses', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}dc-status': {'ignore': True, 'class': 'DCStatusType', 'append': 'dc_statuses', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}version': {'ignore': True, 'class': 'VersionType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}title': {'ignore': True, 'class': 'TextWithSubType', 'append': 'titles', 'min': 1, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}description': {'ignore': True, 'class': 'HTMLTextWithSubType', 'append': 'descriptions', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}reference': {'ignore': True, 'class': 'ReferenceType', 'append': 'references', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}platform': {'ignore': True, 'class': 'OverrideableCPE2IDRefType', 'append': 'platforms', 'min': 0, 'max': None},

            '{http://checklists.nist.gov/xccdf/1.1}select': {'class': 'ProfileSelectType', 'map': 'settings', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}set-value': {'class': 'ProfileSetValueType', 'map': 'settings', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}refine-value': {'class': 'ProfileRefineValueType', 'map': 'settings', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}refine-rule': {'class': 'ProfileRefineRuleType', 'map': 'settings', 'key': 'idref', 'min': 0, 'max': None},

            '{http://checklists.nist.gov/xccdf/1.1}metadata': {'ignore': True, 'class': 'MetadataType', 'append': 'metadata', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': 1},
        },
    }

    def get_extended(self, benchmark):
        try:
            extended = benchmark.profile[self.extends]
        except AttributeError:
            # If any Profile’s extends property identifier does not match the
            # identifier of another Profile in the Benchmark, then Loading
            # fails.
            raise ValueError('Profile ' + self.id + ' unable to extend unknown profile id: ' + self.extends)

        return extended

    def apply(self, items, host):
        ### Benchmark.Profile

        # TODO check that if this group has a platform identified, that the
        # target system matches

        # If a Profile id was specified, then apply the settings in the Profile
        # to the Items of the Benchmark
        for setting_idref in self.settings:
            setting = self.settings[setting_idref]
            try:
                item = items[setting_idref]
            except KeyError:
                raise ValueError('Unable to apply profile setting to idref ' + setting_idref)

            setting.apply(item)
