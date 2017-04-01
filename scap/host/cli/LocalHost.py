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
import os
import selectors
from subprocess import Popen, PIPE
import getpass
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
        inventory = Inventory()

        if sudo:
            if inventory.has_option(self.hostname, 'sudo_password'):
                sudo_password = inventory.get(self.hostname, 'sudo_password')
            else:
                sudo_password = getpass.getpass('Sudo password for host ' + self.hostname + ': ')

            cmd = 'sudo -S -- sh -c "' + cmd.replace('"', r'\"') + '"'

            if sys.platform.startswith('linux'):
                sudo_prompt = '[sudo]'
            elif sys.platform.startswith('darwin'):
                sudo_prompt = 'Password:'
            else:
                raise NotImplementedError('sudo prompt unknown for platform ' + sys.platform)

        logger.debug("Sending command: " + cmd)
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True, universal_newlines=True)

        # note; can't use p.communicate; have to figure out if we get a prompt
        # because there isn't if within sudo timeout
        out_buf = ''
        err_buf = ''
        sel = selectors.DefaultSelector()
        sel.register(p.stdout, selectors.EVENT_READ)
        sel.register(p.stderr, selectors.EVENT_READ)
        while True:
            for (key, events) in sel.select():
                if key.fileobj is p.stdout and events & selectors.EVENT_READ:
                    outs = p.stdout.buffer.read1(1024).decode()
                    if len(outs) > 0:
                        logger.debug('Got stdout: ' + outs)
                        out_buf += outs
                elif key.fileobj is p.stderr and events & selectors.EVENT_READ:
                    errs = p.stderr.buffer.read1(1024).decode()
                    if len(errs) > 0:
                        logger.debug('Got stderr: ' + errs)
                        err_buf += errs
                    if sudo and err_buf.startswith(sudo_prompt):
                        logger.debug("Sending sudo_password...")
                        p.stdin.write(sudo_password + "\n")
                        p.stdin.close()
                        err_buf = ''

            if p.stdout.closed and p.stderr.closed:
                p.stdin.close()
                break

            if p.poll() is not None:
                p.stdin.close()
                break

        sel.unregister(p.stdout)
        sel.unregister(p.stderr)
        sel.close()

        lines = str.splitlines(out_buf)
        err_lines = str.splitlines(err_buf)

        if sudo:
            if len(err_lines) > 0 and err_lines[0].startswith(sudo_prompt):
                del err_lines[0]

        if len(err_lines) > 0:
            raise RuntimeError(str(err_lines))
        return lines
