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

from scap.Model import Model
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class DataStreamCollection(Model):
    def from_xml(self, root_el):
        super(DataStreamCollection, self).from_xml(None, root_el)

        self.components = {}

        # find the specified data stream or the only data stream if none specified
        from scap.model.scap_1_2.DataStream import DataStream
        self.data_streams = {}
        for ds_el in root_el.findall("./scap_1_2:data-stream", Engine.namespaces):
            ds = DataStream()
            ds.from_xml(self, ds_el)
            self.data_streams[ds_el.attrib['id']] = ds

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
