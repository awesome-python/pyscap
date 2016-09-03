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
from scap.model.oval_common_5.ClassEnumeration import CLASS_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class DefinitionType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://www.w3.org/2000/09/xmldsig#}Signature': {'ignore': True, 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}metadata': {'class': 'MetadataType'},
            '{http://oval.mitre.org/XMLSchema/oval-common-5}notes': {'class': 'NotesType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes': {'class': 'NotesType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria': {'class': 'CriteriaType', 'min': 0, 'max': 1},
        },
        'attributes': {
            'id': {'type': 'oval_common_5.DefinitionIDPattern', 'required': True},
            'version': {'type': 'NonNegativeInteger', 'required': True},
            'class': {'enum': CLASS_ENUMERATION, 'required': True},
            'deprecated': {'type': 'Boolean', 'default': False},
        }
    }
