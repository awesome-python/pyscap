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

def negate(value):
    if value == 'true':
        return 'false'
    elif value == 'false':
        return 'true'
    else:
        return value

def count_results(values):
    counts = {
        'true': 0,
        'false': 0,
        'error': 0,
        'unknown': 0,
        'not evaluated': 0,
        'not applicable': 0,
    }
    for val in values:
        counts[val] ++

    return counts['true'], counts['false'], counts['error'], counts['unknown'], \
        counts['not evaluated'], counts['not applicable']

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                || 1+ | 0  | 0  | 0  | 0  | 0+ ||  True
#                || 0+ | 1+ | 0+ | 0+ | 0+ | 0+ ||  False
#       AND      || 0+ | 0  | 1+ | 0+ | 0+ | 0+ ||  Error
#                || 0+ | 0  | 0  | 1+ | 0+ | 0+ ||  Unknown
#                || 0+ | 0  | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def AND(values):
    t, f, e, u, ne, na = count_results(values)
    if t >= 1 and f == 0 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif f >= 1:
        return 'false'
    elif f == 0 and e >= 1:
        return 'error'
    elif f == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif f == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                || 1  | 0+ | 0  | 0  | 0  | 0+ ||  True
#                || 2+ | 0+ | 0+ | 0+ | 0+ | 0+ ||  ** False **
#                || 0  | 1+ | 0  | 0  | 0  | 0+ ||  ** False **
#       ONE      ||0,1 | 0+ | 1+ | 0+ | 0+ | 0+ ||  Error
#                ||0,1 | 0+ | 0  | 1+ | 0+ | 0+ ||  Unknown
#                ||0,1 | 0+ | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def ONE(values):
    t, f, e, u, ne, na = count_results(values)
    if t == 1 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif t >= 2:
        return 'false'
    elif t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif (t == 0 or t == 1) and e >= 1:
        return 'error'
    elif (t == 0 or t == 1) and e == 0 and u >= 1:
        return 'unknown'
    elif (t == 0 or t == 1) and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                || 1+ | 0+ | 0+ | 0+ | 0+ | 0+ ||  True
#                || 0  | 1+ | 0  | 0  | 0  | 0+ ||  False
#       OR       || 0  | 0+ | 1+ | 0+ | 0+ | 0+ ||  Error
#                || 0  | 0+ | 0  | 1+ | 0+ | 0+ ||  Unknown
#                || 0  | 0+ | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def OR(values):
    t, f, e, u, ne, na = count_results(values)
    if t >= 1:
        return 'true'
    elif t == 0 and f >= 1 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif t == 0 and e >= 1:
        return 'error'
    elif t == 0 and e == 0 and u >= 1:
        return 'unknown'
    elif t == 0 and e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'

# ---------------||-----------------------------||------------------
#                ||  num of individual results  ||
#   operator is  ||                             ||  final result is
#                || T  | F  | E  | U  | NE | NA ||
# ---------------||-----------------------------||------------------
#                ||odd | 0+ | 0  | 0  | 0  | 0+ ||  True
#                ||even| 0+ | 0  | 0  | 0  | 0+ ||  False
#       XOR      || 0+ | 0+ | 1+ | 0+ | 0+ | 0+ ||  Error
#                || 0+ | 0+ | 0  | 1+ | 0+ | 0+ ||  Unknown
#                || 0+ | 0+ | 0  | 0  | 1+ | 0+ ||  Not Evaluated
#                || 0  | 0  | 0  | 0  | 0  | 1+ ||  Not Applicable
# ---------------||-----------------------------||------------------
def XOR(values):
    t, f, e, u, ne, na = count_results(values)
    if t % 2 == 1 and e == 0 and u == 0 and ne == 0:
        return 'true'
    elif t % 2 == 0 and e == 0 and u == 0 and ne == 0:
        return 'false'
    elif e >= 1:
        return 'error'
    elif e == 0 and u >= 1:
        return 'unknown'
    elif e == 0 and u == 0 and ne >= 1:
        return 'not evaluated'
    elif t == 0 and f == 0 and e == 0 and u == 0 and ne == 0 and na >= 1:
        return 'not applicable'
