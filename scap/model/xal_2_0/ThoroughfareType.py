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
class ThoroughfareType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'Thoroughfare',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine': {'append': 'address_lines', 'class': 'AddressLineType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumber': {'in': 'thoroughfare_number', 'class': 'ThoroughfareNumberType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberRange': {'in': 'thoroughfare_number_range', 'class': 'ThoroughfareNumberRangeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberPrefix': {'append': 'thoroughfare_number_prefixes', 'class': 'ThoroughfareNumberPrefixType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberSuffix': {'append': 'thoroughfare_number_suffixes', 'class': 'ThoroughfareNumberSuffixType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePreDirection': {'in': 'thoroughfare_pre_direction', 'class': 'ThoroughfarePreDirectionType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareLeadingType': {'in': 'thoroughfare_leading_type', 'class': 'ThoroughfareLeadingTypeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareName': {'append': 'thoroughfare_names', 'class': 'ThoroughfareNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareTrailingType': {'in': 'thoroughfare_trailing_type', 'class': 'ThoroughfareTrailingTypeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePostDirection': {'in': 'thoroughfare_post_direction', 'class': 'ThoroughfarePostDirectionType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentThoroughfare': {'in': 'dependent_thoroughfare', 'class': 'DependentThoroughfareType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocality': {'in': 'dependent_locality', 'class': 'DependentLocalityType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise': {'in': 'premise', 'class': 'PremiseType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm': {'in': 'firm', 'class': 'FirmType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode': {'in': 'postal_code', 'class': 'PostalCodeType'},
            '*': {'ignore': True}
        },
        'attributes': {
            'Type': {},
            'DependentThoroughfares': {'enum': ['Yes', 'No']},
            'DependentThoroughfaresIndicator': {},
            'DependentThoroughfaresConnector': {},
            'DependentThoroughfaresType': {},
            '*': {'ignore': True},
        }
    }
