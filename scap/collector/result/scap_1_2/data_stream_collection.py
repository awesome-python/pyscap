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

from scap.collector.ResultCollector import ResultCollector
import logging

logger = logging.getLogger(__name__)
class data_stream_collection(ResultCollector):
    def collect_results(self):
        if self.args.data_stream:
            ds_name = self.args.data_stream[0]
            if ds_name not in self.content.data_streams:
                logger.critical('Specified --data_stream, ' + ds_name + ', not found in content. Available data streams: ' + str(self.content.data_streams.keys()))
                import sys
                sys.exit()
            else:
                ds = self.content.data_streams[ds_name]
        else:
            if len(self.content.data_streams) == 1:
                ds = self.content.data_streams.values()[0]
            else:
                logger.critical('No --data_stream specified and unable to implicitly choose one. Available data-streams: ' + str(self.content.data_streams.keys()))
                import sys
                sys.exit()
        logger.info('Selecting data stream ' + ds.id)

        self.host.add_result_collector(ResultCollector.load_collector(self.host, ds, self.args))
