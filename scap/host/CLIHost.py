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

from scap.Host import Host
import logging
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class CLIHost(Host):
    def __init__(self, connection):
        super(CLIHost, self).__init__(connection)

    def exec_command(self, cmd):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def line_from_command(self, cmd):
        return self.exec_command(cmd).readline()

    def lines_from_command(self, cmd):
        return self.exec_command(cmd).readlines()
