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
class Catalog(Model, collections.abc.MutableMapping):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:entity:xmlns:xml:catalog',
        'tag_name': 'catalog',
        'attributes': {
            'id': {'ignore': True, 'type': 'ID'},
            'prefer': {'ignore': True, 'enum': ['system', 'public']},
            '*': {'ignore': True}
        },
        'elements': {
            '{urn:oasis:names:tc:entity:xmlns:xml:catalog}uri': {'map': 'entries', 'key': 'name', 'value': 'uri'},
            '*': {'ignore': True},
        },
    }


    def __delitem__(self, key):
        del self.entries[key]

    def __getitem__(self, key):
        return self.entries[key]

    def __setitem__(self, key, value):
        self.entries[key] = value

    def __contains__(self, item):
        return item in self.entries

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries.keys())
