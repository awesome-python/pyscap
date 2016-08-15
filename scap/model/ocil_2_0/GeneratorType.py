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
class GeneratorType(Model):
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/ocil/2.0',
        'tag_name': 'generator',
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}product_name': {'type': 'NormalizedString', 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}product_version': {'type': 'NormalizedString', 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}author': {'append': 'authors', 'class': 'UserType'},
            '{http://scap.nist.gov/schema/ocil/2.0}schema_version': {'type': 'Decimal', 'min': 1, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}timestamp': {'type': 'DateTime', 'min': 1, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}additional_data': {'class': 'AdditionalDataType'},
        }
    }
