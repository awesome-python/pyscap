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

from scap.FactCollector import FactCollector

class WinRMCollector(FactCollector):
    def collect(self):
        ver = self.host.exec_command('ver', [])
        self.host.facts['ver'] = ver
        if uname.startswith('Microsoft Windows'):
            self.host.facts['oval_family'] = 'windows'
        else:
            raise NotImplementedError('Host discovery has not been implemented for winrm ver: ' + ver)
