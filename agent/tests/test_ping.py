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
import ssl
import pytest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from message.Message import Message
from message.PingMessage import PingMessage
from message.PongMessage import PongMessage

HOST = 'localhost'
PORT = 9001

ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.load_verify_locations(cafile='../scanner_cert.pem')
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.check_hostname = True
ctx.load_cert_chain('../scanner_cert.pem', keyfile='../scanner_key.pem')

@pytest.fixture(scope="module")
def s(request):
    with ctx.wrap_socket(
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        server_hostname=socket.gethostbyaddr(HOST)[0]
    ) as s:
        s.connect((HOST, PORT))
        yield s
        s.shutdown(socket.SHUT_RDWR)

def test_ping(s):
    # test Ping/Pong Messages
    req = PingMessage()
    req.send_via(s)
    resp = Message.recv_via(s)
    assert(isinstance(resp, PongMessage))
    assert(req.payload == resp.payload)
