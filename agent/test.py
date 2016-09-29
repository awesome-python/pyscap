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

from Message import Message
from PingMessage import PingMessage

HOST = 'localhost'
PORT = 9001

# logger setup
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(ch_formatter)
rootLogger.addHandler(ch)

logger = logging.getLogger(__name__)

# create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    req = PingMessage()
    try:
        req.send_via(s)
        resp = Message.recv_via(s)
        logger.info('Response: ' + str(resp))
        if req._payload != resp._payload:
            logger.warning('Request payload does not match response')
        else:
            logger.info('Request payload matches response')
    except OSError as e:
        logger.warning('Socket connection broken')
    else:
        logger.info('Closing connection...')
        s.shutdown(socket.SHUT_RDWR)
