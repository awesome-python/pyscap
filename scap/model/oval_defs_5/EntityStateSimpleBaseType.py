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

from scap.model.oval_defs_5.EntitySimpleBaseType import EntitySimpleBaseType
from scap.model.oval_common_5.CheckEnumeration import CHECK_ENUMERATION
from scap.model.oval_common_5.ExistenceEnumeration import EXISTENCE_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class EntityStateSimpleBaseType(EntitySimpleBaseType):
    MODEL_MAP = {
        # abstract
        # TODO <xsd:restriction base="xsd:string"/>
        'attributes': {
            'entity_check': {'enum': CHECK_ENUMERATION, 'default': 'all'},
            'check_existence': {'enum': EXISTENCE_ENUMERATION, 'default': 'at_least_one_exists'},
        }
    }
