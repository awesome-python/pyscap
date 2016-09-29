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

import importlib
import logging
import pickle
import socket
import sys

logger = logging.getLogger(__name__)
class Message():
    MAGIC = b'SCAP'
    VERSION = 1

    TYPES = [
        'ExceptionMessage',
        'PingMessage',
        'PongMessage',
    ]

    def __init__(self, type_, payload):
        self._type = type_
        self._payload = payload

    def send_via(self, sock):
        totalsent = 0
        # send magic
        logger.debug('Sending magic value ' + str(Message.MAGIC) + ', size: ' + str(len(Message.MAGIC)))
        while totalsent < len(Message.MAGIC):
            sent = sock.send(Message.MAGIC[totalsent:])
            logger.debug('Sent ' + str(sent) + ' bytes')
            if sent == 0:
                raise RuntimeError("No data sent, assuming socket connection broken")
            totalsent += sent

        totalsent = 0
        # send version
        logger.debug('Sending version: ' + str(Message.VERSION))
        vers = Message.VERSION.to_bytes(4, byteorder='big')
        while totalsent < len(vers):
            sent = sock.send(vers[totalsent:])
            logger.debug('Sent ' + str(sent) + ' bytes')
            if sent == 0:
                raise RuntimeError("No data sent, assuming socket connection broken")
            totalsent += sent

        totalsent = 0
        # send size
        payload = pickle.dumps(self._payload)
        selfsize = len(payload)
        logger.debug('Sending size: ' + str(selfsize))
        nselfsize = selfsize.to_bytes(4, byteorder='big')
        while totalsent < len(nselfsize):
            sent = sock.send(nselfsize[totalsent:])
            logger.debug('Sent ' + str(sent) + ' bytes')
            if sent == 0:
                raise RuntimeError("No data sent, assuming socket connection broken")
            totalsent += sent

        totalsent = 0
        # send type
        logger.debug('Sending type: ' + str(self._type))
        type_ = self._type.to_bytes(4, byteorder='big')
        while totalsent < len(type_):
            sent = sock.send(type_[totalsent:])
            logger.debug('Sent ' + str(sent) + ' bytes')
            if sent == 0:
                raise RuntimeError("No data sent, assuming socket connection broken")
            totalsent += sent

        totalsent = 0
        # send payload
        logger.debug('Sending payload: ' + str(self._payload))
        while totalsent < len(payload):
            sent = sock.send(payload[totalsent:])
            logger.debug('Sent ' + str(sent) + ' bytes')
            if sent == 0:
                raise RuntimeError("No data sent, assuming socket connection broken")
            totalsent += sent

        logger.debug('Send complete.')

    def __str__(self):
        return 'Message[type=' + str(self._type) + ', payload=' + str(self._payload) + ']'

    @staticmethod
    def recv_via(sock):
        data = b''
        totalrecv = 0
        logger.debug('Reading magic value...')
        while totalrecv < len(Message.MAGIC):
            chunk = sock.recv(len(Message.MAGIC) - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        logger.debug('Testing received magic value ' + str(data) + ' against ' + str(Message.MAGIC) + '...')
        if data != Message.MAGIC:
            raise RuntimeError("Invalid magic value")
        logger.debug('Valid magic value')

        data = b''
        totalrecv = 0
        logger.debug('Reading version...')
        while totalrecv < 4:
            chunk = sock.recv(4 - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        vers = int.from_bytes(data, byteorder='big')
        logger.debug('Received version ' + str(vers) + '...')
        if vers != Message.VERSION:
            raise RuntimeError("Invalid version")
        logger.debug('Valid version')

        data = b''
        totalrecv = 0
        logger.debug('Reading size...')
        while totalrecv < 4:
            chunk = sock.recv(4 - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        selfsize = int.from_bytes(data, byteorder='big')
        logger.debug('Will read message of size: ' + str(selfsize))

        data = b''
        totalrecv = 0
        logger.debug('Reading type...')
        while totalrecv < 4:
            chunk = sock.recv(4 - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        type_ = int.from_bytes(data, byteorder='big')
        logger.debug('Message type: ' + str(type_))

        data = b''
        totalrecv = 0
        logger.debug('Reading payload...')
        while totalrecv < selfsize:
            chunk = sock.recv(selfsize - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        if type_ == 0:
            return ExceptionMessage

        mod = importlib.import_module(Message.TYPES[type_])
        class_ = getattr(mod, Message.TYPES[type_])
        inst = class_(pickle.loads(data))
        return inst
