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

from scap.host.CLIHost import CLIHost
import logging
import sys
import binascii
import os
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class SudoHost(CLIHost):
    def __init__(self, hostname):
        super(SudoHost, self).__init__(hostname)

    def exec_privileged_command(self, cmd):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def can_privileged_command(self):
        inventory = Inventory()
        return inventory.has_option(self.hostname, 'sudo_password')

    def line_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readline()

    def lines_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readlines()
