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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class FileStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'file_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filename': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}owner': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}a_time': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}c_time': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}m_time': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ms_checksum': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}version': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}type': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}development_class': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}company': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}internal_name': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}language': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}original_filename': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}product_name': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}product_version': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}windows_view': {'class': 'oval_defs_5.EntityStateStringType'},
        }
    }
