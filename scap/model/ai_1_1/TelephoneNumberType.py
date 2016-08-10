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

from scap.model.xs.Token import Token
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class TelephoneNumberType(Token):
    # collapsed element telephone-number into telephone-number-type
    # <xs:pattern value="(([2-9][0-8]\d-[2-9]\d{2}-[0-9]{4})|(\+([0-9] ?){6,14}[0-9]))"/>
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/asset-identification/1.1',
        'tag_name': 'telephone-number',
        'attributes': {
            'source': {'class': 'Source'},
            'timestamp': {'class': 'Timestamp'},
            '*': {'ignore': True},
        }
    }
