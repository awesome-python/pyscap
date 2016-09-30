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
from agent.FactsRequestMessage import FactsRequestMessage
from agent.FactsResponseMessage import FactsResponseMessage

HOST = 'localhost'
PORT = 9001

@pytest.fixture(scope="module")
def s(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        yield s
        s.shutdown(socket.SHUT_RDWR)

def test_facts(s):
        req = FactsRequestMessage()
        req.send_via(s)
        resp = Message.recv_via(s)
        assert(isinstance(resp, FactsResponseMessage))
        assert(isinstance(resp.payload, dict))
        assert('os.name' in resp.payload)
