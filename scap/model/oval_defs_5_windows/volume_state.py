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

from scap.model.oval_defs_5.State import State
import logging

logger = logging.getLogger(__name__)
class volume_state(State)
    def __init__(self):
        super(volume_state, self).__init__(
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_state')

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}rootpath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_system',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}name',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}drive_type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_max_component_length',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serial_number',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_case_sensitive_search',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_case_preserved_names',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_unicode_on_disk',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_persistent_acls',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_file_compression',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_volume_quotas',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_sparse_files',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_reparse_points',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_remote_storage',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_volume_is_compressed',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_object_ids',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_encryption',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_named_streams',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_read_only_volume',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_sequential_write_once',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_transactions',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_hard_links',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_extended_attributes',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_open_by_file_id',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_supports_usn_journal',
        ])

