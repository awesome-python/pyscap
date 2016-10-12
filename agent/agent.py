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
import socket
import ssl

from ConnectionThread import ConnectionThread

BIND_ADDRESS = ''
BIND_PORT = 9001
LISTEN_BACKLOG = 5

# logger setup
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="agent.log", mode='w')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
rootLogger.addHandler(ch)
rootLogger.addHandler(fh)

logger = logging.getLogger(__name__)

# ctx = ssl.SSLContext(ssl.PROTOCOL_TLS) # can't use option before 3.5.3
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.options |= ssl.OP_NO_SSLv2
ctx.options |= ssl.OP_NO_SSLv3
ctx.load_verify_locations(cafile='../ca_cert.pem')
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_cert_chain('agent_cert.pem', keyfile='agent_key.pem')
logger.info('Cert Store: ' + str(ctx.cert_store_stats()))

# create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
    # bind the socket to a public host, and a well-known port
    logger.info('Binding to ' + str(BIND_PORT) + ' on address ' + str(BIND_ADDRESS))
    ss.bind((BIND_ADDRESS, BIND_PORT))
    logger.info('Listening for connections...')
    ss.listen(LISTEN_BACKLOG)

    while True:
        # accept connections from outside
        (conn, address) = ss.accept()
        s = ctx.wrap_socket(conn, server_side=True)
        ct = ConnectionThread(s, address)
        ct.start()
