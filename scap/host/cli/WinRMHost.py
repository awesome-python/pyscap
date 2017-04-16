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
from scap.Inventory import Inventory
from winrm.protocol import Protocol
import logging

logger = logging.getLogger(__name__)
class WinRMHost(CLIHost):
    def __init__(self, hostname, args):
        super(WinRMHost, self).__init__(hostname, args)

        self.facts['oval_family'] = 'windows'
        from scap.collector.windows.VerCollector import VerCollector
        self.collectors.append(VerCollector(self))

    def disconnect(self):
        self.protocol.close_shell(self.shell_id)

    def exec_command(self, cmd, args):
        if not isinstance(cmd, str) or not isinstance(args, tuple):
            raise ValueError('WinRM Host needs a str for a command then args tuple')
        command_id = self.protocol.run_command(self.shell_id, cmd, list(args))
        std_out, std_err, status_code = self.protocol.get_command_output(self.shell_id, command_id)
        self.protocol.cleanup_command(self.shell_id, command_id)

        if status_code != 0:
            raise RuntimeError('Command returned non-zero status code: ' + str(status_code) + ' ' + std_err)
        if std_err:
            raise RuntimeError('Command returned std_err: ' + std_err)

        return std_out.decode().splitlines()
