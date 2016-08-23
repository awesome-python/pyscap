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
class RPMVerifyStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#linux',
        'tag_name': 'rpmverify_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}filepath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}size_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}mode_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}md5_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}device_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}link_mismatch',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}ownership_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}group_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}mtime_differs',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}capabilities_differ',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}configuration_file',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}documentation_file',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}ghost_file',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}license_file',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}readme_file',
        }
    }
