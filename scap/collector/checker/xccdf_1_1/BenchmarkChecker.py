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
import datetime

logger = logging.getLogger(__name__)
class BenchmarkChecker(Checker):
    def __init__(self, host, args, model):
        super(BenchmarkChecker, self).__init__(host, args, model)

        host.facts['benchmark'] = {'start_time': datetime.datetime.utcnow()}

        self.model.noticing()

        if args.profile:
            self.selected_profile = args.profile[0]
        else:
            self.selected_profile = None

        self.model.resolve()

    def collect(self):
        self.model.process(self.selected_profile)

        host.facts['benchmark']['end_time'] = datetime.datetime.utcnow()
