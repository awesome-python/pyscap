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
import string, random, socket, logging

logger = logging.getLogger(__name__)
class PSExecHost(Host):
    def __init__(self, hostname, args):
        super(PSExecHost, self).__init__(hostname, args)

        # TODO initialize collectors

    def connect(self):
        inventory = Inventory()
        address = self.hostname
        if inventory.has_option(self.hostname, 'address'):
            address = inventory.get(self.hostname, 'address')
        # TODO

    def disconnect(self):
        pass
