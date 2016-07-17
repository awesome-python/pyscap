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
        super(self.__class__, self).__init__(None, root_el)
        # find the specified data stream or the only data stream if none specified
        self.data_streams = {}

        for ds_el in root_el.findall("./scap_1_2:data-stream", Engine.namespaces):
            self.data_streams[ds_el.attrib['id']] = DataStream(self, ds_el)

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            import sys
            sys.exit()

        if ref[0] == '#':
            ref = ref[1:]
            comp_el = self.element.find("./scap_1_2:component[@id='" + ref + "']", Engine.namespaces)
            if not comp_el:
                logger.critical('unresolved ref: ' + ref)
                import sys
                sys.exit()

            el = list(comp_el)[0]
            if el.tag == '{http://checklists.nist.gov/xccdf/1.2}Benchmark':
                from scap.model.xccdf_1_2.benchmark import Benchmark
                return Benchmark(self, el)
            elif el.tag == '{http://scap.nist.gov/schema/ocil/2.0}ocil':
                from scap.model.ocil_2_0.ocil import OCIL
                return OCIL(self, el)
            elif el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions':
                from scap.model.oval_defs_5.oval_definitions import OVALDefinitions
                return OVALDefinitions(self, el)
            else:
                logger.critical('unknown component: ' + el.tag + ' for ref: ' + ref)
                import sys
                sys.exit()
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
