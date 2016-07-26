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

from scap.model.oval_defs_5_linux.State import State
import logging

logger = logging.getLogger(__name__)
class rpmverifypackage_state(State)
    def __init__(self):
        super(rpmverifypackage_state, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rpmverifypackage_state

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}epoch',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}release',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}arch',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}extended_name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}dependency_check_passed',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}digest_check_passed',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}verification_script_successful',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}signature_check_passed',
        ])
