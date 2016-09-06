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

import logging
import collections.abc

from scap.Model import Model

logger = logging.getLogger(__name__)
class RefListType(Model, collections.abc.MutableMapping):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/scap/source/1.2}component-ref': {'map': 'component_refs', 'class': 'ComponentRefElement'},
        },
    }

    def __delitem__(self, ):
        del self.component_refs[key]

    def __getitem__(self, key):
        return self.component_refs[key]

    def __setitem__(self, key, value):
        self.component_refs[key] = value

    def __contains__(self, item):
        return item in self.component_refs

    def __len__(self):
        return len(self.component_refs)

    def __iter__(self):
        return iter(self.component_refs.keys())
