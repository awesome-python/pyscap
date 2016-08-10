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
class PostalServiceElementsType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'PostalServiceElements',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressIdentifier': {'append': 'address_identifiers', 'class': 'AddressIdentifierType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}EndorsementLineCode': {'class': 'EndorsementLineCodeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}KeyLineCode': {'class': 'KeyLineCodeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Barcode': {'class': 'BarcodeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SortingCode': {'class': 'SortingCodeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLatitude': {'class': 'AddressLatitudeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLatitudeDirection': {'class': 'AddressLatitudeDirectionType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLongitude': {'class': 'AddressLongitudeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLongitudeDirection': {'class': 'AddressLongitudeDirectionType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SupplementaryPostalServiceData': {'class': 'SupplementaryPostalServiceDataType'},
            '*': {'ignore': True},
        },
        'attributes': {
            'Type': {},
            '*': {'ignore': True},
        }
    }
