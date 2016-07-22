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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class DataStreamCollection(Simple):
    def __init__(self):
        super(DataStreamCollection, self).__init__()

        self.components = {}
        self.data_streams = {}

        self.required_attributes.extend([
            'id',
            'schematron-version',
        ])

        self.ignore_attributes.extend([
            'schematron-version',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-component',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}data-stream':
            from scap.model.scap_1_2.DataStream import DataStream
            ds = DataStream()
            ds.from_xml(self, sub_el)
            self.data_streams[sub_el.attrib['id']] = ds
        elif sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}component':
            self.components[sub_el.attrib['id']] = sub_el
        elif sub_el.tag == '{http://www.w3.org/2000/09/xmldsig#}extended-component':
            self.extended_componenets[sub_el.attrib['id']] = sub_el
        else:
            return super(DataStreamCollection, self).parse_sub_el(sub_el)
        return True

    def resolve_reference(self, ref):
        # TODO incorporate simple parsing
        from scap.Engine import Engine
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
                        href = comp_ref_el.attrib['{http://www.w3.org/1999/xlink}href']
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
