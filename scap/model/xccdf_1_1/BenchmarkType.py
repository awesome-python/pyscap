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
            '{http://checklists.nist.gov/xccdf/1.1}model': {'append': 'models', 'class': 'ModelType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}Profile': {'class': 'ProfileType', 'min': 0, 'max': None, 'map': 'profiles'},
            '{http://checklists.nist.gov/xccdf/1.1}Value': {'class': 'ValueType', 'min': 0, 'max': None, 'map': 'items', 'referable': True},
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

    def __str__(self):
        return self.__class__.__name__ + ' # ' + self.id

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
        if self.resolved:
            return
        ### Loading.Resolve.Items

        for item_id in self.items:
            logger.debug('Resolving item: ' + item_id)
            self.items[item_id].resolve(self)

        ### Loading.Resolve.Profiles

        for profile_id in self.profiles:
            if self.profiles[profile_id].extends:
                logger.debug('Resolving profile: ' + profile_id)
                self.profiles[profile_id].resolve(self)

        ### Loading.Resolve.Abstract

        # For each Item in the Benchmark for which the abstract property is
        # true, remove the Item.
        for item_id in self.items:
            if self.items[item_id].abstract:
                logger.debug('Deleting abstract item: ' + item_id)
                del self.items[item_id]

        # For each Profile in the Benchmark for which the abstract property is
        # true, remove the Profile. Go to the next step:
        # Loading.Resolve.Finalize
        for profile_id in self.profiles:
            if self.profiles[profile_id].abstract:
                logger.debug('Deleting abstract profile: ' + profile_id)
                del self.profiles[profile_id]

        ### Loading.Resolve.Finalize

        # Set the Benchmark resolved property to true; Loading succeeds.
        self.resolved = True

    def process(self, host, selected_profile=None):
        ### Benchmark.Front

        # Process the properties of the Benchmark object

        # TODO check that if this benchmark has a platform specification identified,
        # that the  target system matches

        # TODO check that if this benchmark has a platform identified, that the
        # target system matches

        ### Benchmark.Profile

        if selected_profile is None:
            if len(self.profiles) == 0:
                # No profiles; skip the step
                pass
            elif len(self.profiles) == 1:
                selected_profile = list(self.profiles.keys())[0]
            else:
                logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(self.profiles.keys()))
                import sys
                sys.exit()
        else:
            if selected_profile not in self.profiles:
                raise ValueError('Specified --profile, ' + selected_profile + ', not found in content. Available profiles: ' + str(self.profiles.keys()))

        logger.info('Selecting profile ' + str(selected_profile))
        self.profiles[selected_profile].apply(self, host)

        ### Benchmark.Content

        # For each Item in the Benchmark object’s items property, initiate
        # Item.Process
        for item in self.items.values():
            item.process(self, host)

        ### Benchmark.Back

        # Perform any additional processing of the Benchmark object properties
        # TODO


    def _score_model(self, host, model_system, params):
        from scap.model.xccdf_1_1.GroupType import GroupType
        from scap.model.xccdf_1_1.RuleType import RuleType

        if 'scores' not in host.facts:
            host.facts['scores'] = []

        if model_system == 'urn:xccdf:scoring:default':
            ### Score.Group.Init

            # If the node is a Group or the Benchmark, assign a count of 0, a
            # score s of 0.0, and an accumulator a of 0.0.
            count = 0
            score = 0.0
            accumulator = 0.0

            ### Score.Group.Recurse

            # For each selected child of this Group or Benchmark, do the following:
            # (1) compute the count and weighted score for the child using this
            # algorithm,
            # (2) if the child’s count value is not 0, then add the child’s
            # weighted score to this node’s score s, add 1 to this node’s count,
            # and add the child’s weight value to the accumulator a.
            for item_id in self.items:
                item = self.items[item_id]

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                if not item.selected:
                    continue

                item_score = item.score(host)
                if item_score[item_id]['score'] is None:
                    continue

                if item_score[item_id]['count'] != 0:
                    score += item_score[item_id]['score'] * item_score[item_id]['weight']
                    count += 1
                    accumulator += item_score[item_id]['weight']

            ### Score.Group.Normalize

            # Normalize this node’s score: compute s = s / a.
            if accumulator == 0.0:
                if score != 0.0:
                    raise ValueError('Got to score normalization with score ' + str(score) + ' / ' + str(accumulator))
                else:
                    score = 0.0
            else:
                score = score / accumulator

            logger.debug(model_system + ' score: ' + str(score))
            host.facts['scores'].append({'score': score, 'system': model_system})

        elif model_system == 'urn:xccdf:scoring:flat':
            scores = {}
            for item_id in self.items:
                item = self.items[item_id]

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host))

            score = 0.0
            max_score = 0.0
            for rule_id in scores:
                if scores[rule_id]['result'] in ['notapplicable', 'notchecked', 'informational', 'notselected']:
                    continue

                max_score += scores[rule_id]['weight']
                if scores[rule_id]['result'] in ['pass', 'fixed']:
                    score += scores[rule_id]['weight']

            logger.debug(model_system + ' score: ' + str(score) + ' / ' + str(max_score))
            host.facts['scores'].append({'score': score, 'max_score': max_score, 'system': model_system})

        elif model_system == 'urn:xccdf:scoring:flat-unweighted':
            scores = {}
            for item_id in self.items:
                item = self.items[item_id]

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host))

            score = 0.0
            max_score = 0.0
            for rule_id in scores:
                if scores[rule_id]['result'] in ['notapplicable', 'notchecked', 'informational', 'notselected']:
                    continue

                max_score += 1.0
                if scores[rule_id]['result'] in ['pass', 'fixed']:
                    score += 1.0

            logger.debug(model_system + ' score: ' + str(score) + ' / ' + str(max_score))
            host.facts['scores'].append({'score': score, 'max_score': max_score, 'system': model_system})

        elif model_system == 'urn:xccdf:scoring:absolute':
            scores = {}
            for item_id in self.items:
                item = self.items[item_id]

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host))

            score = 0.0
            max_score = 0.0
            for rule_id in scores:
                if scores[rule_id]['result'] in ['notapplicable', 'notchecked', 'informational', 'notselected']:
                    continue

                max_score += scores[rule_id]['weight']
                if scores[rule_id]['result'] in ['pass', 'fixed']:
                    score += scores[rule_id]['weight']

            if score == max_score:
                score = 1.0
            else:
                score = 0.0

            logger.debug(model_system + ' score: ' + str(score))
            host.facts['scores'].append({'score': score, 'system': model_system})

        else:
            raise NotImplementedError('Scoring model ' + model_system + ' is not implemented')

    def score(self, host):
        if len(self.models) == 0:
            self._score_model(host, 'urn:xccdf:scoring:default', [])
            return

        for model in self.models:
            params = {}
            for p in model.params:
                params[p.name] = p.value
            self._score_model(host, model.system, params)
