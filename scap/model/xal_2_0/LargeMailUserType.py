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
class LargeMailUserType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'LargeMailUser',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine': {'append': 'address_lines', 'class': 'AddressLineType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUserName': {'append': 'large_mail_user_names', 'class': 'LargeMailUserNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUserIdentifier': {'in': 'large_mail_user_identifier', 'class': 'LargeMailUserIdentifierType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingName': {'append': 'building_names', 'class': 'BuildingNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Department': {'in': 'department', 'class': 'DepartmentType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox': {'in': 'post_box', 'class': 'PostBoxType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare': {'in': 'thoroughfare', 'class': 'ThoroughfareType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode': {'in': 'postal_code', 'class': 'PostalCodeType'},
            '*': {'ignore': True},
        },
        'attributes': {
            'Type': {},
            '*': {'ignore': True},
        }
    }
