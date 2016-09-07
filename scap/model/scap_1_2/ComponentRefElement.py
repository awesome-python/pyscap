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
class ComponentRefElement(Model):
    MODEL_MAP = {
        'elements': {
            '{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog': {'class': 'Catalog', 'min': 0},
        },
        'attributes': {
            'id': {'required': True, 'type': 'ComponentRefIDPattern'},
            '{http://www.w3.org/1999/xlink}type': {'enum': ['simple'], 'ignore': True},
            '{http://www.w3.org/1999/xlink}href': {'type': 'String', 'required': True},
        },
    }
