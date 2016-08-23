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
class PEHeaderStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'peheader_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}path',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filename',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}header_signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}target_machine_type',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}number_of_sections',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}time_date_stamp',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}pointer_to_symbol_table',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}number_of_symbols',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_optional_header',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_relocs_stripped',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_executable_image',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_line_nums_stripped',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_local_syms_stripped',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_aggresive_ws_trim',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_large_address_aware',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_16bit_machine',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_bytes_reversed_lo',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_32bit_machine',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_debug_stripped',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_removable_run_from_swap',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_system',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_dll',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_up_system_only',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_file_bytes_reveresed_hi',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}magic_number',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}major_linker_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}minor_linker_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_code',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_initialized_data',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_uninitialized_data',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}address_of_entry_point',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}base_of_code',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}base_of_data',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}image_base_address',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}section_alignment',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_alignment',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}major_operating_system_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}minor_operating_system_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}major_image_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}minor_image_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}major_subsystem_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}minor_susbsystem_version',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_image',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_headers',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}checksum',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}subsystem',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dll_characteristics',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_stack_reserve',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_stack_commit',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_heap_reserve',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}size_of_heap_commit',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}loader_flags',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}number_of_rva_and_sizes',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}real_number_of_directory_entries',
        }
    }
