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

from scap.model.content import Content
import logging
from scap.engine.engine import Engine
from scap.model.scap_1_2.data_stream import DataStream

logger = logging.getLogger(__name__)
class DataStreamCollection(Content):
    def __init__(self, root_el):
        # find the specified data stream or the only data stream if none specified
        self.data_streams = {}

        for ds_el in root.findall("./scap_1_2:data-stream", Engine.namespaces):
            self.data_streams[ds_el.attrib['id']] = DataStream(root, ds_el)

    def select_rules(self, args):
        # b_args = {}
        # if args.data_stream:
        #     b_args['data_stream'] = args.data_stream[0]
        #     if args.checklist:
        #         b_args['checklist'] = args.checklist[0]
        # if args.profile:
        #     b_args['profile'] = args.profile[0]

        # if 'data_stream' in args:
        #     if args['data_stream'] not in data_streams:
        #         logger.critical('Specified --data_stream, ' + args['data_stream'] + ', not found in content. Available data streams: ' + str(data_streams.keys()))
        #         sys.exit()
        #     else:
        #         self.data_stream = data_streams[args['data_stream']]
        # else:
        #     if len(data_streams) == 1:
        #         self.data_stream = data_streams.values()[0]
        #     else:
        #         logger.critical('No --data_stream specified and unable to implicitly choose one. Available data-streams: ' + str(data_streams.keys()))
        #         sys.exit()
        # logger.info('Using data stream ' + self.data_stream.attrib['id'])

        pass
