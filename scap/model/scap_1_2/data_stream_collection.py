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

logger = logging.getLogger(__name__)
class DataStreamCollection(Content):
    def __init__(self, root_el):
        super(self.__class__, self).__init__(None, root_el)

        self.components = {}

        # find the specified data stream or the only data stream if none specified
        from scap.model.scap_1_2.data_stream import DataStream
        self.data_streams = {}
        for ds_el in root_el.findall("./scap_1_2:data-stream", Engine.namespaces):
            self.data_streams[ds_el.attrib['id']] = DataStream(self, ds_el)

        # TODO data stream contains supported dictionaries, checklists, and checks

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            ref = self.ref_mapping[ref]

        if ref[0] == '#':
            ref = ref[1:]
            if ref not in self.components:
                comp_el = self.element.find("./scap_1_2:component[@id='" + ref + "']", Engine.namespaces)
                if comp_el is not None:
                    self.components[ref] = list(comp_el)[0]
                else:
                    comp_ref_el = self.element.find(".//scap_1_2:component-ref[@id='" + ref + "']", Engine.namespaces)
                    if comp_ref_el is not None:
                        href = comp_ref_el.attrib['{' + Engine.namespaces['xlink'] + '}href']
                        self.components[ref] = self.resolve_reference(href)
                    else:
                        logger.critical('unresolved ref: ' + ref)
                        import sys
                        sys.exit()

            return self.components[ref]
        else:
            logger.critical('only local references are supported: ' + ref)
            import sys
            sys.exit()

    def select_rules(self, args):
        if args.data_stream:
            data_stream = args.data_stream[0]
            if data_stream not in self.data_streams:
                logger.critical('Specified --data_stream, ' + data_stream + ', not found in content. Available data streams: ' + str(self.data_streams.keys()))
                sys.exit()
            else:
                logger.info('Selecting data stream ' + data_stream)
                return self.data_streams[data_stream].select_rules(args)
        else:
            if len(self.data_streams) == 1:
                ds = self.data_streams.values()[0]
                logger.info('Selecting data stream ' + ds.id)
                return ds.select_rules(args)
            else:
                logger.critical('No --data_stream specified and unable to implicitly choose one. Available data-streams: ' + str(self.data_streams.keys()))
                sys.exit()
