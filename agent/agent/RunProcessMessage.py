#!/usr/bin/env python

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

import logging
import subprocess

from agent.Message import Message
from agent.CompletedProcessMessage import CompletedProcessMessage

logger = logging.getLogger(__name__)
class RunProcessMessage(Message):
    def __init__(self, payload):
        if not isinstance(payload, dict) or 'args' not in payload \
            or not (isinstance(payload['args'], str) \
            or isinstance(payload['args'], list)):
            raise RuntimeError('Invalid arguments specified for run')
        super().__init__(payload)

        args = payload['args']

        # we don't supply stdin pip; ProcessOpenMessage can be used for that
        stdin = None
        # we collect stdout & stderr by default though
        stdout = subprocess.PIPE
        stderr = subprocess.PIPE

        input_ = None
        if 'input' in payload:
            input_ = payload['input']

        shell = False
        if 'shell' in payload and payload['shell']:
            shell = True

        timeout = None
        if 'timeout' in payload:
            timeout = payload['timeout']

        self.completed_process = subprocess.run(args, stdin=stdin, input=input_, \
            stdout=stdout, stderr=stderr, shell=shell, timeout=timeout)

    def respond_via(self, sock):
        resp = CompletedProcessMessage({
            'args': self.completed_process.args,
            'returncode': self.completed_process.returncode,
            'stdout': self.completed_process.stdout,
            'stderr': self.completed_process.stderr,
        })
        resp.send_via(sock)
