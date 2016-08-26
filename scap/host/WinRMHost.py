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

        from scap.fact_collector.WinRMCollector import WinRMCollector
        self.fact_collectors.append(WinRMCollector(self))

    def connect(self):
        inventory = Inventory()
        if inventory.has_option(self.hostname, 'username') and inventory.has_option(self.hostname, 'password'):
            username = inventory.get(self.hostname, 'username')
            password = inventory.get(self.hostname, 'password')
            if inventory.has_option(self.hostname, 'port'):
                port = inventory.get(self.hostname, 'port')
                self.session = winrm.Session('http://' + self.hostname + ':' + port, auth=(username, password))
            else:
                self.session = winrm.Session('http://' + self.hostname, auth=(username, password))
        else:
            raise RuntimeError('No method of authenticating with host ' + self.hostname + ' found')

    def disconnect(self):
        pass

    def exec_command(self, cmd):
        if not isinstance(cmd, tuple) or not isinstance(cmd[0], str) or not isinstance(cmd[1], list):
            raise RuntimeError('WinRM Host needs a tuple for a command; cmd str then args list')
        r = self.session.run_cmd(cmd[0], cmd[1])
        
