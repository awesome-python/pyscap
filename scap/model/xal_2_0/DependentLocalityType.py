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
class DependentLocalityType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'DependentLocality',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine': {'append': 'address_lines', 'class': 'AddressLineType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocalityName': {'append': 'address_lines', 'class': 'LocalityNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocalityNumber': {'append': 'address_lines', 'class': 'DependentLocalityNumberType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox': {'in': 'post_box', 'class': 'PostBoxType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUser': {'in': 'large_mail_user', 'class': 'LargeMailUserType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOffice': {'in': 'post_office', 'class': 'PostOfficeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRoute': {'in': 'post_route', 'class': 'PostalRouteType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare': {'in': 'thoroughfare', 'class': 'ThoroughfareType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise': {'in': 'premise', 'class': 'PremiseType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocality': {'in': 'premise', 'class': 'DependentLocalityType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode': {'in': 'postal_code', 'class': 'PostalCodeType'},
            '*': {'ignore': True},
        },
        'attributes': {
            'Type': {},
            'UsageType': {},
            'Connector': {},
            'Indicator': {},
            '*': {'ignore': True},
        }
    }
