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
class fileauditedpermissions53_state(State)
    def __init__(self):
        super(fileauditedpermissions53_state, self).__init__(
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_state')

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filename',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}trustee_sid',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_delete',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_read_control',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_dac',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_write_owner',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}standard_synchronize',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}access_system_security',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_read',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_write',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_execute',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}generic_all',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_data',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_write_data',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_append_data',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_ea',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_write_ea',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_execute',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_delete_child',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_attributes',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_write_attributes',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}windows_view',
        ])

