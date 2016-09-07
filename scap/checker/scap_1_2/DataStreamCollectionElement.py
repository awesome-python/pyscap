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
class DataStreamCollectionElement(Checker):
    def __init__(self, host, content, parent, args=None):
        super(DataStreamCollectionElement, self).__init__(host, content, parent, args)

        if 'data_stream' in args:
            ds_name = args['data_stream']
            if ds_name not in content.data_streams:
                logger.critical('Specified --data_stream, ' + ds_name + ', not found in content. Available data streams: ' + str(list(content.data_streams.keys())))
                import sys
                sys.exit()
            else:
                ds = content.data_streams[ds_name]
        else:
            if len(content.data_streams) == 1:
                ds = list(content.data_streams.values())[0]
            else:
                logger.critical('No --data_stream specified and unable to implicitly choose one. Available data-streams: ' + str(list(content.data_streams.keys())))
                import sys
                sys.exit()
        logger.info('Selecting data stream ' + ds.id)

        self.ds_checker = Checker.load(host, ds, self, args)

    def check(self):
        return self.ds_checker.check()

    def resolve_reference(self, ref):
        if ref[0] == '#':
            ref = ref[1:]
            if ref in self.content.components:
                return self.content.components[ref]

            logger.debug('Reference ' + ref + ' not in components; checking selected data stream')
            return self.ds_checker.resolve_reference('#' + ref)
        else:
            logger.critical('only local references are supported: ' + ref)
            import sys
            sys.exit()
