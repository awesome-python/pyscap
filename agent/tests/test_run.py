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

import socket
import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from agent.Message import Message
from agent.RunProcessMessage import RunProcessMessage
from agent.CompletedProcessMessage import CompletedProcessMessage
from agent.ExceptionMessage import ExceptionMessage

HOST = 'localhost'
PORT = 9001

@pytest.fixture(scope="module")
def s(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        yield s
        s.shutdown(socket.SHUT_RDWR)

def test_response(s):
    req = RunProcessMessage({
        'args': 'exit',
        'shell': True,
    })
    req.send_via(s)
    resp = Message.recv_via(s)

    assert(isinstance(resp, CompletedProcessMessage))
    assert(isinstance(resp.payload, dict))

    assert('args' in resp.payload)
    assert('returncode' in resp.payload)
    assert('stdout' in resp.payload)
    assert('stderr' in resp.payload)

def test_reg_query(s):
    req = RunProcessMessage({
        'args': 'REG QUERY HKLM\Software\Microsoft\Windows\CurrentVersion /v ProgramFilesDir',
    })
    req.send_via(s)
    resp = Message.recv_via(s)

    assert(resp.payload['returncode'] == 0)
    assert(b'Program Files' in resp.payload['stdout'])
    assert(resp.payload['stderr'] == b'')

def test_returncode(s):
    req = RunProcessMessage({
        'args': 'exit 1',
        'shell': True,
    })
    req.send_via(s)
    resp = Message.recv_via(s)

    assert(resp.payload['returncode'] == 1)


def test_timeout(s):
    req = RunProcessMessage({
        'args': 'pause',
        'shell': True,
        'timeout': 1,
    })
    req.send_via(s)
    resp = Message.recv_via(s)

    assert(isinstance(resp, ExceptionMessage))
