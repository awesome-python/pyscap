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

from scap.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class Benchmark(Checker):
    def __init__(self, host, content, args=None):
        super(Benchmark, self).__init__(host, content, args)

        if args.profile:
            profile_id = args.profile[0]
            if profile_id not in self.content.profiles:
                logger.critical('Specified --profile, ' + profile_id + ', not found in content. Available profiles: ' + str(self.content.profiles.keys()))
                import sys
                sys.exit()
            else:
                profile = self.content.profiles[profile_id]
        else:
            if len(self.content.profiles) == 1:
                profile = self.content.profiles.values()[0]
            else:
                logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(self.content.profiles.keys()))
                import sys
                sys.exit()
        logger.info('Selecting profile ' + profile.id)

        self.profile_checker = Checker.load(self.host, profile)

    def check(self):
        return self.profile_checker.check()
