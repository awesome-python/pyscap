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

from scap.collector.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class BenchmarkChecker(Checker):
    def __init__(self, host, args, content):
        super(BenchmarkChecker, self).__init__(host, host, args, content)

        ### Loading.Noticing
        # For each notice property of the Benchmark object, add the notice to
        # the tool’s set of legal notices. If a notice with an identical id
        # value is already a member of the set, then replace it. If the
        # Benchmark’s resolved property is set, then Loading succeeds, otherwise
        # go to the next step: Loading.Resolve.Items.

        for notice in list(self.content.notices.values()):
            logger.info('Notice: \n' + str(notice))

        ### Loading.Resolve.Items
        for item in self.content.items.values():
            item.resolve(self.content)

        ### Loading.Resolve.Profiles
        # For each Profile in the Benchmark that has an extends property,
        # resolve the set of properties in the extending Profile by applying the
        # following steps:
        # (1) resolve the extended Profile,
        # (2) prepend the property sequence from the extended Profile to that of
        # the extending Profile,
        # (3) remove all but the last instance of duplicate properties.
        # If any Profile’s extends property identifier does not match the
        # identifier of another Profile in the Benchmark, then Loading fails. If
        # the directed graph formed by the extends properties of Profiles
        # includes a loop, then Loading fails. Otherwise, go to
        # Loading.Resolve.Abstract.

        ### Loading.Resolve.Abstract
        # For each Item in the Benchmark for which the abstract property is
        # true, remove the Item. For each Profile in the Benchmark for which the
        # abstract property is true, remove the Profile. Go to the next step:
        # Loading.Resolve.Finalize.
        for item in self.content.items.values():
            item.process()

        ### Loading.Resolve.Finalize
        # Set the Benchmark resolved property to true; Loading succeeds.

        ### Benchmark.Front
        # Process the properties of the Benchmark object

        ### Benchmark.Profile
        # If a Profile id was specified, then apply the settings in the Profile
        # to the Items of the Benchmark

        if args.profile:
            profile_id = args.profile[0]
            if profile_id not in content.profiles:
                logger.critical('Specified --profile, ' + profile_id + ', not found in content. Available profiles: ' + str(list(content.profiles.keys())))
                import sys
                sys.exit()

            self.selected_profile = args.profile[0]
        else:
            if len(content.profiles) == 1:
                self.selected_profile = list(content.profiles.keys())[0]
            else:
                logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(list(content.profiles.keys())))
                import sys
                sys.exit()
        logger.info('Selecting profile ' + self.selected_profile)

        if self.content.profiles[self.selected_profile].extends:
            raise NotImplementedError('Profiles with @extend are not supported')

        ### Benchmark.Content
        # For each Item in the Benchmark object’s items property, initiate
        # Item.Process
        for item in self.content.items.values():
            item.process()

        ### Benchmark.Back
        # Perform any additional processing of the Benchmark object properties

        ### Item.Process
        # Check the contents of the requires and conflicts properties, and if
        # any required Items are unselected or any conflicting Items are
        # selected, then set the selected and allowChanges properties to false.

        ### Item.Select
        # If any of the following conditions holds, cease processing of this
        # Item:
        # 1. The processing type is Tailoring, and the optional property and
        # selected property are both false.
        # 2. The processing type is Document Generation, and the hidden property
        # is true.
        # 3. The processing type is Compliance Checking, and the selected
        # property is false.
        # 4. The processing type is Compliance Checking, and the current
        # platform (if known by the tool) is not a member of the set of
        # platforms for this Item.

        ### Group.Front
        # If the Item is a Group, then process the properties of the Group.

        ### Group.Content
        # If the Item is a Group, then for each Item in the Group’s items
        # property, initiate Item.Process.

        ### Rule.Content
        # If the Item is a Rule, then process the properties of the Rule.

        ### Value.Content
        # If the Item is a Value, then process the properties of the Value.

        ### Default Model
        # urn:xccdf:scoring:default

            ### Score.Rule

            ### Score.Group.Init

            ### Score.Group.Recurse

            ### Score.Group.Normalize

            ### Score.Weight

        ### Flat Model
        # urn:xccdf:scoring:flat

            ### Score.Init

            ### Score.Rules

        ### Flat Unweighted Model
        # urn:xccdf:scoring:flat-unweighted

        ### Absolute Model
        # urn:xccdf:scoring:absolute

    def collect(self):
