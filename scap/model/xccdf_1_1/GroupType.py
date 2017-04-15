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

from scap.model.xccdf_1_1.SelectableItemType import SelectableItemType
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class GroupType(SelectableItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'GroupIDPattern'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}Value': {'class': 'ValueType', 'map': 'items', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}Group': {'class': 'GroupType', 'map': 'items', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}Rule': {'class': 'RuleType', 'map': 'items', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': 1},
        },
    }

    def resolve(self, benchmark):
        ### Loading.Resolve.Items

        # For each Item in the Benchmark that has an extends property, resolve
        # it by using the following steps:
        if self.extends is None:
            return

        # (1) if the Item is Group, resolve all the enclosed Items,
        for item_id in self.items:
            self.items[item_id].resolve(benchmark)

        # (2) resolve the extended Item,
        extended = self.get_extended(benchmark)
        extended.resolve(benchmark)

        # (3) prepend the property sequence from the extended Item to the
        # extending Item,
        # (5) remove duplicate properties and apply property overrides, and
        for name in self.model_map['attributes']:
            attr_map = self.model_map['attributes'][name]
            if 'ignore' in attr_map and attr_map['ignore']:
                continue

            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xml_namespace, attr_name = Model.parse_tag(name)
                attr_name = attr_name.replace('-', '_')
            self.resolve_property(extended, attr_name)

        for tag in self.model_map['elements']:
            xml_namespace, tag_name = Model.parse_tag(tag)
            if tag.endswith('*'):
                continue

            tag_map = self.model_map['elements'][tag]
            if 'ignore' in tag_map and tag_map['ignore']:
                continue

            if 'append' in tag_map:
                self.resolve_property(extended, tag_map['append'])
            elif 'map' in tag_map:
                self.resolve_property(extended, tag_map['map'])
            else:
                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = tag_name.replace('-', '_')
            self.resolve_property(extended, name)

        # (4) if the Item is a Group, assign values for the id properties of
        # Items copied from the extended Group,
        if hasattr(extended, 'items') and len(extended.items) > 0:
            for ext_item in extended.items:
                # make a copy of the item and append to our items
                self.items.append(ext_item.copy())

        # (6) remove the extends property.
        self.extends = None

        # If the directed graph formed by the extends properties includes a
        # loop, then Loading fails.
        # TODO

        # Otherwise, go to the next step: Loading.Resolve.Profiles.

    def process(self, benchmark, host):
        super(GroupType, self).process(benchmark, host)

        if not self._continue_processing():
            return

        ### Group.Front

        # If the Item is a Group, then process the properties of the Group.
        # TODO

        # TODO check that if this group has a platform identified, that the
        # target system matches

        ### Group.Content

        # If the Item is a Group, then for each Item in the Group’s items
        # property, initiate Item.Process.
        for item_id in self.items:
            self.items[item_id].process(benchmark, host)

        # TODO result retention

    def score(self, host, model = 'urn:xccdf:scoring:default'):
        from scap.model.xccdf_1_1.RuleType import RuleType

        if model == 'urn:xccdf:scoring:default':
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

                if not item.selected:
                    continue

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                item_score = item.score(host)
                if item_score[item_id]['score'] is None:
                    continue

                if item_score[item_id]['count'] != 0:
                    score += item_score[item_id]['score'] * item_score[item_id]['weight']
                    count += 1
                    accumulator += item_score[item_id]['weight']

            ### Score.Group.Normalize

            # Normalize this node’s score: compute s = s / a
            if accumulator == 0.0:
                if score != 0.0:
                    raise ValueError('Got to score normalization with score ' + str(score) + ' / ' + str(accumulator))
                else:
                    score = 0.0
            else:
                score = score / accumulator

            ### Score.Weight

            # Assign the node a weighted score equal to the product of its score
            # and its weight.
            # (done upstream)

            return {self.id: {'model': model, 'score': score, 'weight': self.weight, 'count': count}}

        elif model == 'urn:xccdf:scoring:flat' \
        or model == 'urn:xccdf:scoring:flat-unweighted' \
        or model == 'urn:xccdf:scoring:absolute':
            scores = {}
            for item_id in self.items:
                item = self.items[item_id]

                if not item.selected:
                    continue

                if not isinstance(item, GroupType) \
                and not isinstance(item, RuleType):
                    continue

                # just pass the scores upstream for processing
                scores.update(item.score(host))
            return scores

        else:
            raise NotImplementedError('Scoring model ' + model + ' is not implemented')
