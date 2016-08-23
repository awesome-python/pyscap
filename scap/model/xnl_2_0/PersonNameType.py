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
class PersonNameType(Model):
    MODEL_MAP = {
        'xml_namespace': 'urn:oasis:names:tc:ciq:xsdschema:xNL:2.0',
        'tag_name': 'PersonName',
        'elements': {
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}NameLine': {'append': 'name_lines', 'class': 'NameLineType'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}PrecedingTitle': {'append': 'preceding_titles', 'class': 'PrecedingTitleElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}Title': {'append': 'titles', 'class': 'TitleElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}FirstName': {'append': 'first_names', 'class': 'FirstNameElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}MiddleName': {'append': 'middle_names', 'class': 'MiddleNameElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}NamePrefix': {'in': 'name_prefix', 'class': 'NamePrefixElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}LastName': {'append': 'last_names', 'class': 'LastNameElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}OtherName': {'append': 'other_names', 'class': 'OtherNameElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}Alias': {'append': 'aliases', 'class': 'AliasElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}GenerationIdentifier': {'append': 'generation_identifiers', 'class': 'GenerationIdentifierElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}Suffix': {'append': 'suffixes', 'class': 'SuffixElement'},
            '{urn:oasis:names:tc:ciq:xsdschema:xNL:2.0}GeneralSuffix': {'append': 'general_suffix', 'class': 'GeneralSuffixElement'},
        },
        'attributes': {
            'Type': {},
            'Code': {},
            'NameDetailsKeyRef': {}, # from grKeyRefs
            '*': {'ignore': True},
        }
    }
