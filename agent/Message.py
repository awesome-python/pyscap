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
        'FactsRequestMessage',
        'FactsResponseMessage',
    ]
    REVERSE_TYPES = None

    def __init__(self, payload):
        if Message.REVERSE_TYPES is None:
            Message.REVERSE_TYPES = {Message.TYPES[n]: n for n in range(len(Message.TYPES))}

        try:
            self._type = Message.REVERSE_TYPES[self.__class__.__name__]
        except NameError as e:
            raise RuntimeError('Unregistered Message type: ' + self.__class__.__name__)
        self._payload = payload

    def send_via(self, sock):
        msg = b''

        # send magic
        logger.debug('Adding magic value ' + str(Message.MAGIC))
        msg += Message.MAGIC

        # send version
        vers = Message.VERSION.to_bytes(4, byteorder='big')
        logger.debug('Adding version: ' + str(Message.VERSION) + '(' + str(vers) + ')')
        msg += vers

        # send size
        bpayload = pickle.dumps(self._payload)
        selfsize = len(bpayload)
        bselfsize = selfsize.to_bytes(4, byteorder='big')
        logger.debug('Adding payload size: ' + str(selfsize) + '(' + str(bselfsize) + ')')
        msg += bselfsize

        # send type
        btype = self._type.to_bytes(4, byteorder='big')
        logger.debug('Adding type: ' + str(self._type) + '(' + str(btype) + ')')
        msg += btype

        # send payload
        logger.debug('Adding payload...')
        #logger.debug('Adding payload: ' + str(self._payload) + '(' + str(bpayload) + ')')
        msg += bpayload

        # send the whole message atomicly
        logger.debug('Sending message...')
        totalsent = 0
        while totalsent < len(msg):
            sent = sock.send(msg[totalsent:])
            logger.debug('Sent ' + str(sent) + ' bytes of message')
            if sent == 0:
                raise RuntimeError("No data sent, assuming socket connection broken")
            totalsent += sent

        logger.debug('Send complete.')

    def __str__(self):
        return self.__class__.__name__ + '[type=' + str(self._type) + ', payload=' + str(self._payload) + ']'

    @staticmethod
    def recv_via(sock):
        data = b''
        totalrecv = 0
        logger.debug('Receiving magic value...')
        while totalrecv < len(Message.MAGIC):
            chunk = sock.recv(len(Message.MAGIC) - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        logger.debug('Magic: ' + str(data))
        if data != Message.MAGIC:
            raise RuntimeError("Invalid magic value")

        data = b''
        totalrecv = 0
        logger.debug('Receiving version...')
        while totalrecv < 4:
            chunk = sock.recv(4 - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        vers = int.from_bytes(data, byteorder='big')
        logger.debug('Version: ' + str(data) + '(' + str(vers) + ')...')
        if vers != Message.VERSION:
            raise RuntimeError("Invalid version")

        data = b''
        totalrecv = 0
        logger.debug('Receiving payload size...')
        while totalrecv < 4:
            chunk = sock.recv(4 - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        selfsize = int.from_bytes(data, byteorder='big')
        logger.debug('Payload size: ' + str(data) + '(' + str(selfsize) + ')')

        data = b''
        totalrecv = 0
        logger.debug('Receiving type...')
        while totalrecv < 4:
            chunk = sock.recv(4 - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        type_ = int.from_bytes(data, byteorder='big')
        logger.debug('Message type: ' + str(data) + '(' + str(type_) + ')')
        if type_ < 0 or type_ >= len(Message.TYPES):
            raise RuntimeError('Unknown type code: ' + str(type_))

        data = b''
        totalrecv = 0
        logger.debug('Receiving payload...')
        while totalrecv < selfsize:
            chunk = sock.recv(selfsize - totalrecv)
            if chunk == b'':
                raise RuntimeError("No data received, assuming socket connection broken")
            data += chunk
            totalrecv += len(chunk)

        payload = pickle.loads(data)
        #logger.debug('Payload: ' + str(data) + '(' + str(payload) + ')')
        logger.debug('Received payload.')

        mod = importlib.import_module(Message.TYPES[type_])
        class_ = getattr(mod, Message.TYPES[type_])
        inst = class_(payload)
        return inst
