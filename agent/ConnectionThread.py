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
from threading import Thread

from Message import Message
from PingMessage import PingMessage
from ExceptionMessage import ExceptionMessage

logger = logging.getLogger(__name__)
class ConnectionThread(Thread):
    def __init__(self, conn, address):
        super().__init__()

        logger.info("Connection from " + str(address))
        self._socket = conn
        self._address = address

    def run(self):
        with self._socket:
            try:
                while True:
                    try:
                        req = Message.recv_via(self._socket)
                        logger.info('Received message: ' + str(req))
                        if isinstance(req, PingMessage):
                            req.respond_via(self._socket)
                        else:
                            raise RuntimeError('Unknown message type: ' + req._type)
                    except RuntimeError as e:
                        resp = ExceptionMessage(e)
                        resp.send_via(self._socket)
            except OSError as e:
                logger.info('Socket connection broken with ' + str(self._address) + ' due to ' + str(e))
            else:
                logger.info('Connection to ' + str(self._address) + ' closing...')
                self._socket.shutdown(socket.SHUT_RDWR)
        logger.info('Connection to ' + str(self._address) + ' closed')
