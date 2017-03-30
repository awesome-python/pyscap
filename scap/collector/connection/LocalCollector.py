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

from scap.Collector import Collector
import logging
import sys
import subprocess
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class LocalCollector(Collector):
    def __init__(self, hostname, args):
        super(LocalCollector, self).__init__(hostname, args)

        if sys.platform.startswith('linux') or sys.platform == 'cygwin':
            from scap.collector.cli.unix.UNameCollector import UNameCollector
            self.host.collectors.append(UNameCollector(self.host))
        elif sys.platform == 'win32':
            self.facts['oval_family'] = 'windows'
            from scap.collector.cli.windows.VerCollector import VerCollector
            self.host.collectors.append(VerCollector(self.host))

    def exec_command(self, cmd):
        logger.debug("Sending command: " + 'sh -c "' + cmd.replace('"', r'\"') + '"')
        stdin, stdout, stderr = self.client.exec_command('sh -c "' + cmd.replace('"', r'\"') + '"')

        err = stderr.read()
        if err.strip():
            raise RuntimeError(err)
        return stdout

    def exec_privileged_command(self, cmd):
        inventory = Inventory()
        if not self.can_privileged_command():
            raise RuntimeError("Can't run privileged command without sudo_password defined in credentials")
        logger.debug("Sending command: " + 'sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"')
        stdin, stdout, stderr = self.client.exec_command('sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"')

        logger.debug("Sending sudo_password...")
        stdin.write(inventory.get(self.hostname, 'sudo_password') + "\n")
        # eat the prompt
        stderr.readline()

        err = stderr.read()
        if err.strip():
            raise RuntimeError(err)
        return stdout
