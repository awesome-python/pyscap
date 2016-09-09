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

EXISTENCE_ENUMERATION = [
    'all_exist',
    'any_exist',
    'at_least_one_exists',
    'none_exist',
    'only_one_exists',
]

EXISTENCE_RESULT_ENUMERATION = [
    'exists',
    'does not exist',
    'error',
    'not collected',
]

def count_item_status_values(item_status_values):
    counts = {}
    for i in EXISTENCE_RESULT_ENUMERATION:
        counts[i] = 0

    for v in item_status_values:
        counts[v] += 1

    return counts['exists'], counts['does not exist'], counts['error'], counts['not collected']

def all_exist(item_status_values):
    exists, does_not_exist, error, not_collected = count_item_status_values(item_status_values)

    if exists >= 1 and does_not_exist == 0 and error == 0 and not_collected == 0:
        return 'true'
    elif exists == 0 and does_not_exist == 0 and error == 0 and not_collected == 0:
        return 'false'
    elif does_not_exist >= 1:
        return 'false'
    elif does_not_exist == 0 and error >= 1:
        return 'error'
    elif does_not_exist == 0 and error == 0 and not_collected >= 1:
        return 'unknown'

def any_exist(item_status_values):
    exists, does_not_exist, error, not_collected = count_item_status_values(item_status_values)

    if error == 0:
        return 'true'
    elif exists >= 1 and error >= 1:
        return 'true'
    elif exists == 0 and error >= 1:
        return 'error'

def at_least_one_exists(item_status_values):
    exists, does_not_exist, error, not_collected = count_item_status_values(item_status_values)

    if exists >= 1:
        return 'true'
    elif exists == 0 and does_not_exist >= 1 and error == 0 and not_collected == 0:
        return 'false'
    elif exists == 0 and error >= 1:
        return 'error'
    elif exist == 0 and error == 0 and not_collected >= 1:
        return 'unknown'

def none_exist(item_status_values):
    exists, does_not_exist, error, not_collected = count_item_status_values(item_status_values)

    if exists == 0 and error == 0 and not_collected == 0:
        return 'true'
    elif exists >= 1:
        return 'false'
    elif exists == 0 and error >= 1:
        return 'error'
    elif exists == 0 and error == 0 and not_collected >= 1:
        return 'unknown'

def only_one_exists(item_status_values):
    exists, does_not_exist, error, not_collected = count_item_status_values(item_status_values)

    if exists == 1 and error == 0 and not_collected == 0:
        return 'true'
    elif exists >= 2:
        return 'false'
    elif exists == 0 and error == 0 and not_collected == 0:
        return 'false'
    elif (exists == 0 or exists == 1) and error >= 1:
        return 'error'
    elif (exists == 0 or exists == 1) and error == 0 and not_collected >= 1:
        return 'unknown'
