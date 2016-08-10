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
class AddressDetailsType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'AddressDetails',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalServiceElements': {'class': 'PostalServiceElementsType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Address': {'class': 'AddressType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLines': {
                'list': 'address_lines',
                'classes': {
                    '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine': 'AddressLineType',
                    '*': None,
                }
            },
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Country': {'class': 'CountryType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AdministrativeArea': {'class': 'AdministrativeAreaType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Locality': {'class': 'LocalityType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare': {'class': 'ThoroughfareType'},
        },
        'attributes': {
            'AddressType': {},
            'CurrentStatus': {},
            'ValidFromDate': {},
            'ValidToDate': {},
            'Usage': {},
            'Code': {}, # from grPostal
            'AddressDetailsKey': {},
            '*': {'ignore': True},
        }
    }
