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

from scap.Collector import Collector
import logging

logger = logging.getLogger(__name__)
class ResultCollector(Collector):
    @staticmethod
    def learn(host, content, args):
        from scap.model.scap_1_2.DataStreamCollection import DataStreamCollection
        if isinstance(content, DataStreamCollection):
            from scap.collector.result.scap_1_2.DataStreamCollectionCollector import DataStreamCollectionCollector
            dsc = DataStreamCollectionCollector(host, content, args)
            return dsc
        else:
            logger.critical('Collector not found for content: ' + content.__class__.__name__)
            sys.exit()

    def __init__(self, host, content):
        super(ResultCollector, self).__init__(host)

        self.content = content

    def collect_results(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
