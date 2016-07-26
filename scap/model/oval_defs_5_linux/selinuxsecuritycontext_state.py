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
class selinuxsecuritycontext_state(State)
    def __init__(self):
        super(selinuxsecuritycontext_state, self).__init__(
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}selinuxsecuritycontext_state')

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}filepath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}path',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}filename',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}pid',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}user',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}role',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}low_sensitivity',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}low_category',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}high_sensitivity',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}high_category',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rawlow_sensitivity',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rawlow_category',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rawhigh_sensitivity',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}rawhigh_category',
        ])

