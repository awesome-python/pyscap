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

AND_TABLE = {}
# ------------------------------------------------------
#    AND             || P | F | U | E | N | K | S | I ||
# -------------------||-------------------------------||
#           Pass (P) || P | F | U | E | P | P | P | P ||
AND_TABLE['pass'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'pass',
    'notchecked': 'pass',
    'notselected': 'pass',
    'informational': 'pass',
}
#           Fail (F) || F | F | F | F | F | F | F | F ||
AND_TABLE['fail'] = {
    'pass': 'fail',
    'fail': 'fail',
    'unknown': 'fail',
    'error': 'fail',
    'notapplicable': 'fail',
    'notchecked': 'fail',
    'notselected': 'fail',
    'informational': 'fail',
}
#        Unknown (U) || U | F | U | U | U | U | U | U ||
AND_TABLE['unknown'] = {
    'pass': 'unknown',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'unknown',
    'notapplicable': 'unknown',
    'notchecked': 'unknown',
    'notselected': 'unknown',
    'informational': 'unknown',
}
#          Error (E) || E | F | U | E | E | E | E | E ||
AND_TABLE['error'] = {
    'pass': 'error',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'error',
    'notchecked': 'error',
    'notselected': 'error',
    'informational': 'error',
}
#  Notapplicable (N) || P | F | U | E | N | N | N | N ||
AND_TABLE['notapplicable'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notapplicable',
    'notselected': 'notapplicable',
    'informational': 'notapplicable',
}
#     Notchecked (K) || P | F | U | E | N | K | K | K ||
AND_TABLE['notchecked'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notchecked',
    'notselected': 'notchecked',
    'informational': 'notchecked',
}
#    Notselected (S) || P | F | U | E | N | K | S | S ||
AND_TABLE['notselected'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notchecked',
    'notselected': 'notselected',
    'informational': 'notselected',
}
#  Informational (I) || P | F | U | E | N | K | S | I ||
AND_TABLE['informational'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notchecked',
    'notselected': 'notselected',
    'informational': 'informational',
}
# ------------------------------------------------------
def AND(left, right):
    return AND_TABLE[left][right]

OR_TABLE = {}
# ------------------------------------------------------
#     OR             || P | F | U | E | N | K | S | I ||
# -------------------||-------------------------------||
#           Pass (P) || P | P | P | P | P | P | P | P ||
OR_TABLE['pass'] = {
    'pass': 'pass',
    'fail': 'pass',
    'unknown': 'pass',
    'error': 'pass',
    'notapplicable': 'pass',
    'notchecked': 'pass',
    'notselected': 'pass',
    'informational': 'pass',
}
#           Fail (F) || P | F | U | E | F | F | F | F ||
OR_TABLE['fail'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'fail',
    'notchecked': 'fail',
    'notselected': 'fail',
    'informational': 'fail',
}
#        Unknown (U) || P | U | U | U | U | U | U | U ||
OR_TABLE['unknown'] = {
    'pass': 'pass',
    'fail': 'unknown',
    'unknown': 'unknown',
    'error': 'unknown',
    'notapplicable': 'unknown',
    'notchecked': 'unknown',
    'notselected': 'unknown',
    'informational': 'unknown',
}
#          Error (E) || P | E | U | E | E | E | E | E ||
OR_TABLE['error'] = {
    'pass': 'pass',
    'fail': 'error',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'error',
    'notchecked': 'error',
    'notselected': 'error',
    'informational': 'error',
}
#  Notapplicable (N) || P | F | U | E | N | N | N | N ||
OR_TABLE['notapplicable'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notapplicable',
    'notselected': 'notapplicable',
    'informational': 'notapplicable',
}
#     Notchecked (K) || P | F | U | E | N | K | K | K ||
OR_TABLE['notchecked'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notchecked',
    'notselected': 'notchecked',
    'informational': 'notchecked',
}
#    Notselected (S) || P | F | U | E | N | K | S | S ||
OR_TABLE['notselected'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notchecked',
    'notselected': 'notselected',
    'informational': 'notselected',
}
#  Informational (I) || P | F | U | E | N | K | S | I ||
OR_TABLE['informational'] = {
    'pass': 'pass',
    'fail': 'fail',
    'unknown': 'unknown',
    'error': 'error',
    'notapplicable': 'notapplicable',
    'notchecked': 'notchecked',
    'notselected': 'notselected',
    'informational': 'informational',
}
# ------------------------------------------------------
def OR(left, right):
    return OR_TABLE[left][right]

# ---------------------------------------
# NOT || P | F | U | E | N | K | S | I ||
# ----||-------------------------------||
#     || F | P | U | E | N | K | S | I ||
# ---------------------------------------
def negate(value):
    if value == 'pass':
        return 'fail'
    elif value == 'fail':
        return 'pass'
    else:
        return value
