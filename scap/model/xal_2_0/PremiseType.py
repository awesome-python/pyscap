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
class PremiseType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0',
        'tag_name': 'Premise',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine': {'append': 'address_lines', 'class': 'AddressLineType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseName': {'append': 'premise_names', 'class': 'PremiseNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseLocation': {'in': 'premise_location', 'class': 'PremiseLocationType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumber': {'append': 'premise_numbers', 'class': 'PremiseNumberType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberRange': {'in': 'premise_number_range', 'class': 'PremiseNumberRangeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberPrefix': {'append': 'premise_number_prefixes', 'class': 'PremiseNumberPrefixType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberSuffix': {'append': 'premise_number_suffixes', 'class': 'PremiseNumberSuffixType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingName': {'append': 'building_names', 'class': 'BuildingNameType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremise': {'append': 'sub_premises', 'class': 'SubPremiseType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm': {'in': 'firm', 'class': 'FirmType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStop': {'in': 'mail_stop', 'class': 'MailStopType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode': {'in': 'postal_code', 'class': 'PostalCodeType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise': {'in': 'premise', 'class': 'PremiseType'},
            '*': {'ignore': True},
        },
        'attributes': {
            'Type': {},
            'PremiseDependency': {},
            'PremiseDependencyType': {},
            'PremiseThoroughfareConnector': {},
            '*': {'ignore': True},
        }
    }
