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
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filename',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}owner',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}a_time',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}c_time',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}m_time',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ms_checksum',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}development_class',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}company',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}internal_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}language',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}original_filename',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}product_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}product_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}windows_view',
        }
    }
