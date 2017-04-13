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
    def __init__(self, host, args, benchmark):
        super(BenchmarkChecker, self).__init__(host, host, args, benchmark)

        host.facts['benchmark'] = {'start_time': datetime.now()}

        benchmark.noticing()

        if args.profile:
            self.selected_profile = args.profile[0]
        else:
            self.selected_profile = None

        benchmark.resolve()

    def collect(self):
        benchmark = self.content

        benchmark.process(self.selected_profile)

        host.facts['benchmark']['end_time'] = datetime.now()
