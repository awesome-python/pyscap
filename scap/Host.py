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

import inspect, urllib.parse, logging
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class Host(object):
    def __init__(self, hostname):
        self.hostname = hostname
        self.collectors = []
        self.resources = {}
        self.facts = {
            'oval_family': 'undefined',
        }
        self.results = {}

        inventory = Inventory()

        # TODO better connection detection
        if not inventory.has_section(hostname) or not inventory.has_option(hostname, 'connection'):
            if hostname == 'localhost':
                connection_type = 'local'
            else:
                connection_type = 'ssh'
        else:
            connection_type = inventory.get(hostname, 'connection')

        # TODO impacket
        # TODO SMB?
        # TODO PSExec?
        if connection_type == 'ssh':
            from scap.collector.connection.SSHCollector import SSHCollector
            self.collectors.append(SSHCollector(self))
        elif connection_type == 'winrm':
            from scap.collector.connection.WinRMCollector import WinRMCollector
            self.collectors.append(WinRMCollector(self))
        elif connection_type == 'local':
            from scap.collector.connection.LocalCollector import LocalCollector
            self.collectors.append(LocalCollector(self))
        else:
            raise RuntimeError('Unsupported host connection type: ' + connection_type)


    def get_hostname(self):
        return self.hostname

    def collect(self):
        # have to use while vs. for loop so collectors can add other collectors
        i = 0
        while i < len(self.collectors):
            try:
                self.collectors[i].collect()
            except Exception as e:
                import traceback
                logger.warning('Fact collector ' + self.collectors[i].__class__.__name__ + ' failed: ' + e.__class__.__name__ + ' ' + str(e) + ':\n' + traceback.format_exc())
            i += 1
