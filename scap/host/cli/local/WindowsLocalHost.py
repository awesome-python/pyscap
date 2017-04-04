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

from scap.host.cli.LocalHost import LocalHost
import logging
import sys
import os
import selectors
import subprocess
import getpass
import ctypes

from scap.Inventory import Inventory

logger = logging.getLogger(__name__)
class WindowsLocalHost(LocalHost):
    def detect_collectors(self):
        from scap.collector.cli.WindowsCollector import WindowsCollector
        return [WindowsCollector(self)]

    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def exec_command(self, cmd, elevate=False):
        inventory = Inventory()

        logger.debug("Sending command: " + cmd)
        if elevate:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", 'cmd', '/c "' + cmd.replace('"', r'\"') + '"', None, 1)
        else:
            p = subprocess.run(cmd,
                stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                shell=True)

        #logger.debug('Got stdout: ' + str(p.stdout))
        #logger.debug('Got stderr: ' + str(p.stderr))

        lines = str.splitlines(p.stdout.replace(b'\r\r', b'\r').decode())
        err_lines = str.splitlines(p.stderr.replace(b'\r\r', b'\r').decode())

        #logger.debug('stdout lines: ' + str(lines))
        #logger.debug('stderr lines: ' + str(err_lines))

        if len(err_lines) > 0:
            raise RuntimeError(str(err_lines))
        return lines
