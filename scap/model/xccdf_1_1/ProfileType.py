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

            '{http://checklists.nist.gov/xccdf/1.1}select': {'class': 'ProfileSelectType', 'map': 'selects', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}set-complex-value': {'class': 'ProfileSetComplexValueType', 'map': 'set_complex_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}set-value': {'class': 'ProfileSetValueType', 'map': 'set_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}refine-value': {'class': 'ProfileRefineValueType', 'map': 'refine_values', 'key': 'idref', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}refine-rule': {'class': 'ProfileRefineRuleType', 'map': 'refine_rules', 'key': 'idref', 'min': 0, 'max': None},

            '{http://checklists.nist.gov/xccdf/1.1}metadata': {'ignore': True, 'class': 'MetadataType', 'append': 'metadata', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': 1},
        },
    }

    def resolve(self, benchmark):
        ### Loading.Resolve.Profiles

        # For each Profile in the Benchmark that has an extends property,
        if self.extends == '':
            return

        try:
            extended_profile = benchmark.profiles[self.extends]

            # resolve the set of properties in the extending Profile by applying the
            # following steps:
            # (1) resolve the extended Profile,
            extended_profile.resolve(benchmark)

            # (2) prepend the property sequence from the extended Profile to that of
            # the extending Profile,
            # (3) remove all but the last instance of duplicate properties.
            selects = extended_profile.selects.copy()
            selects.update(self.selects)
            self.selects = selects

            set_complex_values = extended_profile.selects.copy()
            set_complex_values.update(self.set_complex_values)
            self.set_complex_values = set_complex_values

            set_values = extended_profile.selects.copy()
            set_values.update(self.set_values)
            self.set_values = set_values

            refine_values = extended_profile.selects.copy()
            refine_values.update(self.refine_values)
            self.refine_values = refine_values

            refine_rules = extended_profile.selects.copy()
            refine_rules.update(self.refine_rules)
            self.refine_rules = refine_rules
        except AttributeError:

            # If any Profile’s extends property identifier does not match the
            # identifier of another Profile in the Benchmark, then Loading fails.
            raise ValueError('Profile ' + self.id + ' unable to extend unknown profile: ' + self.extends)

        # If the directed graph formed by the extends properties of Profiles
        # includes a loop, then Loading fails.
        # TODO

        # Otherwise, go to Loading.Resolve.Abstract.

    def apply(self, items):
        ### Benchmark.Profile

        # If a Profile id was specified, then apply the settings in the Profile
        # to the Items of the Benchmark
        # TODO

        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
