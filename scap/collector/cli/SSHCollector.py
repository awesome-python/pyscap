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

from scap.collector.CLICollector import CLICollector
import logging

logger = logging.getLogger(__name__)
class SSHCollector(CLICollector):
    def collect(self):
        try:
            from scap.collector.cli.UNameCollector import UNameCollector
            UNameCollector(self.host).collect()
            if self.host.facts['uname'].startswith('Linux'):
                from scap.collector.cli.LinuxCollector import LinuxCollector
                LinuxCollector(self.host).collect()
            # elif uname.startswith('Darwin'):
            #     pass
            elif self.host.facts['uname'].startswith('Windows NT'):
                from scap.collector.cli.WindowsCollector import WindowsCollector
                WindowsCollector(self.host).collect()
            else:
                raise NotImplementedError('Host discovery has not been implemented for uname: ' + self.host.facts['uname'] + ' on ' + self.host.hostname)
        except:
            # uname didn't work
            raise NotImplementedError('Host discovery has not been implemented for host: ' + self.host.hostname)
