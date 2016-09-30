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

from agent.ConnectionThread import ConnectionThread

BIND_ADDRESS = ''
BIND_PORT = 9001
LISTEN_BACKLOG = 5

# logger setup
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="agent.log", mode='w')
fh_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(fh_formatter)
ch_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(ch_formatter)
rootLogger.addHandler(ch)
rootLogger.addHandler(fh)

logger = logging.getLogger(__name__)

# ctx = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
#
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
        ct = ConnectionThread(conn, address)
        ct.start()
