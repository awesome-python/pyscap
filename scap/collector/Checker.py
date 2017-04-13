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

import importlib
import logging
import sys
from scap.Collector import Collector

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
class Checker(Collector):
    @staticmethod
    def load(host, args, content):
        if content.tag == '{http://checklists.nist.gov/xccdf/1.1}Benchmark':
            from scap.collector.checker.xccdf_1_1.BenchmarkChecker import BenchmarkChecker
            return BenchmarkChecker(host, args, content)
        else:
            raise NotImplementedError('Checking with ' + content.tag + ' content has not been implemented')

    def __init__(self, host, args, content):
        super(Checker, self).__init__(host, args)
        self.content = content

    def collect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
