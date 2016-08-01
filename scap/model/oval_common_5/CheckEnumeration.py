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

CHECK_ENUMERATION = [
    'true',
    'false',
    'error',
    'unknown',
    'not evaluated',
    'not applicable',
]

def count_results(results):
    counts = {
        'true': 0,
        'false': 0,
        'error': 0,
        'unknown': 0,
        'not evaluated': 0,
        'not applicable': 0,
    }
    for r in results:
        counts[r] += 1
    return counts['true'], counts['false'], counts['error'], counts['unknown'], counts['not evaluated'], counts['not applicable']

def all(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_results(results)

    if true >= 1 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'true'
    elif false >= 1:
        return 'false'
    elif false == 0 and error >= 1:
        return 'error'
    elif false == 0 and error == 0 and unknown >= 1:
        return 'unknown'
    elif false == 0 and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

def at_least_one(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_results(results)

    if true >= 1:
        return 'true'
    elif true == 0 and false >= 1 and error == 0 and unknown == 0 not_evaluated == 0:
        return 'false'
    elif true == 0 and error >= 1:
        return 'error'
    elif true == 0 and error == 0 and unknown >= 1:
        return 'unknown'
    elif true == 0 and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

def none_satisfy(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_results(results)

    if true == 0 and false >= 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'true'
    elif true >= 1:
        return 'false'
    elif true == 0 and error >= 1:
        return 'error'
    elif true == 0 and error == 0 and unknown >= 1:
        return 'unknown'
    elif true == 0 and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'

def only_one(results):
    true, false, error, unknown, not_evaluated, not_applicable = count_results(results)

    if true == 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'true'
    elif true >= 1:
        return 'false'
    elif true == 0 and false >= 1 and error == 0 and unknown == 0 and not_evaluated == 0:
        return 'false'
    elif (true == 0 or true == 1) and error >=1:
        return 'error'
    elif (true == 0 or true == 1) and error == 0 and unknown >= 1:
        return 'unknown'
    elif (true == 0 or true == 1) and error == 0 and unknown == 0 and not_evaluated >= 1:
        return 'not evaluated'
    elif true == 0 and false == 0 and error == 0 and unknown == 0 and not_evaluated == 0 and not_applicable >= 1:
        return 'not applicable'
