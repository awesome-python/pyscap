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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class PremiseNumberRangeType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'PremiseNumberRange',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberRangeFrom': {'in': 'premise_number_from', 'class': 'PremiseNumberRangeFromType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberRangeTo': {'in': 'premise_number_to', 'class': 'PremiseNumberRangeToType'},
        },
        'attributes': {
            'RangeType': {},
            'Indicator': {},
            'Separator': {},
            'Type': {},
            'IndicatorOccurrence': {'enum': ['Before', 'After']},
            'NumberRangeOccurrence': {'enum': ['BeforeName', 'AfterName', 'BeforeType', 'AfterType']},
        }
    }
