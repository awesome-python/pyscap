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

logger = logging.getLogger(__name__)
class data_stream_collection(Model):
    def __init__(self):
        super(data_stream_collection, self).__init__()    # {http://scap.nist.gov/schema/scap/source/1.2}data-stream-collection

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
            self.data_streams[sub_el.attrib['id']] = Model.load_child(self, sub_el)
        elif sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}component':
            self.components[sub_el.attrib['id']] = Model.load_child(self, sub_el)
        else:
            return super(data_stream_collection, self).parse_sub_el(sub_el)
        return True

    def resolve_reference(self, ref):
        if ref[0] == '#':
            ref = ref[1:]
            if ref not in self.components:
                logger.critical('Reference ' + ref + ' not in ' + str(self.components.keys()))
                import sys
                sys.exit()
            return self.components[ref]
        else:
            logger.critical('only local references are supported: ' + ref)
            import sys
            sys.exit()
