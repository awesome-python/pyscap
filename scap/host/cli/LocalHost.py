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
import subprocess
from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class LocalHost(CLIHost):
    def __init__(self, hostname):
        super(LocalHost, self).__init__(hostname)

        self.enable_mode = False

        if sys.platform.startswith('linux') or sys.platform == 'cygwin':
            from scap.collector.cli.unix.UNameCollector import UNameCollector
            self.collectors.append(UNameCollector(self))
        elif sys.platform == 'win32':
            self.facts['oval_family'] = 'windows'
            from scap.collector.cli.windows.VerCollector import VerCollector
            self.collectors.append(VerCollector(self))
        else:
            raise NotImplementedError('Local connection on ' + sys.platform + ' is not yet supported')

    def connect(self):
        pass

    def disconnect(self):
        pass

    def exec_command(self, cmd, sudo=False):
        if sudo:
            if not inventory.has_option(self.hostname, 'sudo_password'):
                raise RuntimeError("Can't run privileged command without sudo_password defined in credentials")
            cmd = 'sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"'

        logger.debug("Sending command: " + cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        if sudo:
            logger.debug("Sending sudo_password...")
            p.stdin.write(inventory.get(self.hostname, 'sudo_password') + "\n")
            # eat the prompt
            p.stderr.readline()

        outs, errs = p.communicate()

        if errs.strip():
            raise RuntimeError(errs)
        return str.splitlines(outs)
