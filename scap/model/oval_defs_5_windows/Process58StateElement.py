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
class Process58StateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'process58_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}command_line': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}pid': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ppid': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}priority': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_path': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}current_dir': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}creation_time': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dep_enabled': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}primary_window_text': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}name': {'class': 'oval_defs_5.EntityStateStringType'},
        }
    }
