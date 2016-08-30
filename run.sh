#!/bin/bash

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

die() { echo "$0: $@ at ${BASH_SOURCE[1]}:${FUNCNAME[1]} line ${BASH_LINENO[0]}." >& 2; exit 1; }
warn() { echo "$0: $@ at ${BASH_SOURCE[1]}:${FUNCNAME[1]} line ${BASH_LINENO[0]}." >& 2; }

#./pyscap.py -vvv --inventory ~/pyscap_inventory.ini --host localhost --benchmark --content sample_content/USGCB-Windows/scap_gov.nist_USGCB-ie8.xml --pretty
#./pyscap.py -vvv --inventory ~/pyscap_inventory.ini --host iago_8_1_winrm --connect
./pyscap.py -vvv --inventory ~/pyscap_inventory.ini --host iago_8_1_winrm --benchmark --content sample_content/USGCB-Windows/scap_gov.nist_USGCB-ie8.xml --pretty
#./pyscap.py -vvv --inventory ~/pyscap_inventory.ini --host iago_8_1_smb --connect
#./pyscap.py -vvv --inventory ~/pyscap_inventory.ini --host iago_8_1_smb --benchmark --content sample_content/USGCB-Windows/scap_gov.nist_USGCB-ie8.xml --pretty
