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

SCORING_MODEL_ENUMERATION = [
    'urn:xccdf:scoring:default',
    # This specifies the default (XCCDF 1.0) scoring model.
    'urn:xccdf:scoring:flat',
    # This specifies the flat, weighted scoring model.
    'urn:xccdf:scoring:flat-unweighted',
    # This specifies the flat scoring model with weights ignored (all
    # weights set to 1).
    'urn:xccdf:scoring:absolute',
    # This specifies the absolute (1 or 0) scoring model.
]
