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
class SubPremiseType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'SubPremise',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine': {'append': 'address_lines', 'class': 'AddressLineType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseName': {'append': 'sub_premise_names', 'class': 'SubPremiseNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseLocation': {'in': 'sub_premise_location', 'class': 'SubPremiseLocationType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseNumber': {'append': 'sub_premise_numbers', 'class': 'SubPremiseNumberType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseNumberPrefix': {'append': 'sub_premise_number_prefixes', 'class': 'SubPremiseNumberPrefixType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseNumberSuffix': {'append': 'sub_premise_number_suffixes', 'class': 'SubPremiseNumberSuffixType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingName': {'append': 'building_names', 'class': 'BuildingNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm': {'in': 'firm', 'class': 'FirmType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStop': {'in': 'firm', 'class': 'MailStopType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode': {'in': 'postal_code', 'class': 'PostalCodeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremise': {'append': 'sub_premises', 'class': 'SubPremiseType'},
            '*': {'ignore': True},
        },
        'attributes': {
            'Type': {},
            '*': {'ignore': True},
        }
    }
