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

import inspect, urllib.parse, logging
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class Host(object):
    def __init__(self, hostname):
        self.hostname = hostname
        self.fact_collectors = []
        self.facts = {
            'oval_family': 'undefined',
        }


    def get_hostname(self):
        return self.hostname

    def connect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def disconnect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def collect_facts(self):
        # have to use while vs. for loop so collectors can add other collectors
        i = 0
        while i < len(self.fact_collectors):
            try:
                self.fact_collectors[i].collect()
            except Exception as e:
                import traceback
                logger.warning('Fact collector ' + self.fact_collectors[i].__class__.__name__ + ' failed: ' + e.__class__.__name__ + ' ' + str(e) + ':\n' + traceback.format_exc())
            i += 1

    def benchmark(self, content, args):
        from scap.Checker import Checker
        col = Checker.load(self, content, args)
        self.results = col.check()
