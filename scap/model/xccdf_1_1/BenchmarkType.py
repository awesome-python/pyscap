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
class BenchmarkType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}status': {'append': 'statuses', 'class': 'StatusType', 'min': 1, 'max': None, 'ignore': True},
            '{http://purl.org/dc/elements/1.1/}dc-status': {'append': 'dc_statuses', 'class': 'DCStatusType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}title': {'append': 'titles', 'class': 'TextType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}description': {'append': 'descriptions', 'class': 'HTMLTextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}notice': {'map': 'notices', 'class': 'NoticeType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}front-matter': {'append': 'front_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}rear-matter': {'append': 'rear_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}reference': {'append': 'references', 'class': 'ReferenceType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}plain-text': {'append': 'plain_texts', 'class': 'PlainTextType', 'min': 0, 'max': None, 'ignore': True},
            '{http://cpe.mitre.org/language/2.0}platform-specification': {'class': 'scap.model.cpe_2_3.PlatformSpecificationType', 'min': 0, 'max': 1, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}platform': {'class': 'CPE2IDRefType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}version': {'class': 'VersionType', 'min': 1, 'max': 1, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}metadata': {'append': 'metadata', 'class': 'MetadataType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}model': {'append': 'models', 'class': 'ModelType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.1}Profile': {'class': 'ProfileType', 'min': 0, 'max': None, 'map': 'profiles'},
            '{http://checklists.nist.gov/xccdf/1.1}Value': {'class': 'ValueType', 'min': 0, 'max': None, 'map': 'items'},
            '{http://checklists.nist.gov/xccdf/1.1}Group': {'class': 'GroupType', 'min': 0, 'max': None, 'map': 'items'},
            '{http://checklists.nist.gov/xccdf/1.1}Rule': {'class': 'RuleType', 'min': 0, 'max': None, 'map': 'items'},
            '{http://checklists.nist.gov/xccdf/1.1}TestResult': {'class': 'TestResultType', 'min': 0, 'max': None, 'map': 'test_results'},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'class': 'SignatureType', 'min': 0, 'max': 1, 'ignore': True},
        },
        'attributes': {
            'id': {'required': True, 'type': 'BenchmarkIDPattern'},
            'Id': {'ignore': True, 'type': 'ID'},
            'resolved': {'type': 'Boolean', 'default': False},
            'style': {'ignore': True, 'type': 'String'},
            'style-href': {'ignore': True, 'type': 'AnyURI'},
        },
    }

    def noticing(self):
        ### Loading.Noticing

        # For each notice property of the Benchmark object, add the notice to
        # the tool’s set of legal notices. If a notice with an identical id
        # value is already a member of the set, then replace it. If the
        # Benchmark’s resolved property is set, then Loading succeeds, otherwise
        # go to the next step: Loading.Resolve.Items.

        for notice in list(self.notices.values()):
            logger.info('Notice: \n' + str(notice))

    def resolve(self):
        ### Loading.Resolve.Items

        for item in self.items.values():
            item.resolve(self, benchmark)

        ### Loading.Resolve.Profiles

        for profile_id in self.profiles:
            if self.profiles[profile_id].extends:
                self.profiles[profile_id].resolve(self)

        ### Loading.Resolve.Abstract

        # For each Item in the Benchmark for which the abstract property is
        # true, remove the Item.
        for item_id in self.items:
            if self.items[item_id].abstract:
                del self.items[item_id]

        # For each Profile in the Benchmark for which the abstract property is
        # true, remove the Profile. Go to the next step:
        # Loading.Resolve.Finalize
        for profile_id in self.profiles:
            if self.profiles[profile_id].abstract:
                del self.profiles[profile_id]

        ### Loading.Resolve.Finalize

        # Set the Benchmark resolved property to true; Loading succeeds.
        self.resolved = True

    def process(self, selected_profile=None):
        ### Benchmark.Front

        # Process the properties of the Benchmark object
        # TODO

        ### Benchmark.Profile

        if selected_profile is None:
            if len(self.profiles) == 0:
                # No profiles; skip the step
                pass
            elif len(self.profiles) == 1:
                selected_profile = list(self.profiles.keys())[0]
            else:
                logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(list(content.profiles.keys())))
                import sys
                sys.exit()
        else:
            if selected_profile not in self.profiles:
                raise ValueError('Specified --profile, ' + selected_profile + ', not found in content. Available profiles: ' + str(list(content.profiles.keys())))

        if selected_profile is not None:
            logger.info('Selecting profile ' + selected_profile)
            self.profiles[selected_profile].apply(self.items)

        ### Benchmark.Content

        # For each Item in the Benchmark object’s items property, initiate
        # Item.Process
        for item in self.items.values():
            item.process(self)

        ### Benchmark.Back

        # Perform any additional processing of the Benchmark object properties
        # TODO
