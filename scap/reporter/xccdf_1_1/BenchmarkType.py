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

from scap.Reporter import Reporter
import logging

logger = logging.getLogger(__name__)
class BenchmarkType(Reporter):
    def __init__(self, content, hosts, args={}):
        super(BenchmarkType, self).__init__(content, hosts, args)

        # if 'profile' in args:
        #     profile_id = args['profile']
        #     if profile_id not in content.profiles:
        #         logger.critical('Specified --profile, ' + profile_id + ', not found in content. Available profiles: ' + str(list(content.profiles.keys())))
        #         import sys
        #         sys.exit()
        #     else:
        #         profile = content.profiles[profile_id]
        # else:
        #     if len(content.profiles) == 1:
        #         profile = list(content.profiles.values())[0]
        #     else:
        #         logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(list(content.profiles.keys())))
        #         import sys
        #         sys.exit()
        # logger.info('Selecting profile ' + profile.id)

        # self.reporter = R.load(host, profile, self, args)

    def report(self, host):
        return self.reporter.report(host)
