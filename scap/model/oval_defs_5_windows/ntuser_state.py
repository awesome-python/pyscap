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

from scap.model.oval_defs_5_windows.State import State
import logging

logger = logging.getLogger(__name__)
class ntuser_state(State)
    def __init__(self):
        super(ntuser_state, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_state

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}username',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}account_type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logged_on',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}enabled',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}date_modified',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}days_since_modified',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}last_write_time',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}value',
        ])
