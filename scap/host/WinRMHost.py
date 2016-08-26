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
from scap.Inventory import Inventory
import winrm, logging

logger = logging.getLogger(__name__)
class WinRMHost(Host):
    def __init__(self, hostname):
        super(WinRMHost, self).__init__(hostname)

        # TODO initialize collectors

    def connect(self):
        inventory = Inventory()
        if inventory.has_option(self.hostname, 'username') and inventory.has_option(self.hostname, 'password'):
            username = inventory.get(self.hostname, 'username')
            password = inventory.get(self.hostname, 'password')
            self.session = winrm.Session('http://' + self.hostname + ':' + self.port + '/wsman', auth=(username, password))
        else:
            raise RuntimeError('No method of authenticating with host ' + self.hostname + ' found')

    def disconnect(self):
        pass

    # def exec_command(self, cmd):
    #     import inspect
    #     raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    # def can_privileged_command(self):
    #     import inspect
    #     raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    # def exec_privileged_command(self):
    #     import inspect
    #     raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
