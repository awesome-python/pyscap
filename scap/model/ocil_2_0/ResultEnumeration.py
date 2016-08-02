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

RESULT_ENUMERATION = [
    'PASS',
    'FAIL',

    # exceptionals
    'UNKNOWN',
    'ERROR',
    'NOT_TESTED',
    'NOT_APPLICABLE',
]

#         || P   | F | E | U | NT | NA ||
#         ---------------||-----------------------------||------------------||------------------------------------------
#         || 1+ | 0   | 0   | 0   | 0   | 0+ || Pass
#         || 0+ | 1+ | 0+ | 0+ | 0+ | 0+ || Fail
# AND     || 0+ | 0   | 1+ | 0+ | 0+ | 0+ || Error
#         || 0+ | 0   | 0   | 1+ | 0+ | 0+ || Unknown
#         || 0+ | 0   | 0   | 0   | 1+ | 0+ || Not Tested
#         || 0   | 0   | 0   | 0   | 0   | 1+ || Not Applicable
#         || 0   | 0   | 0   | 0   | 0   | 0   || Not Tested

#     ---------------||-----------------------------||------------------||------------------------------------------
#     || 1+ | 0+ | 0+ | 0+ | 0+ | 0+ || Pass
#     || 0   | 1+ | 0   | 0   | 0   | 0+ || Fail
# OR  || 0   | 0+ | 1+ | 0+ | 0+ | 0+ || Error
#     || 0   | 0+ | 0   | 1+ | 0+ | 0+ || Unknown
#     || 0   | 0+ | 0   | 0   | 1+ | 0+ || Not Tested
#     || 0   | 0   | 0   | 0   | 0   | 1+ || Not Applicable
#     || 0   | 0   | 0   | 0   | 0   | 0   || Not Tested
