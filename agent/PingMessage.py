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
import random
import sys

from Message import Message
from PongMessage import PongMessage

logger = logging.getLogger(__name__)
class PingMessage(Message):
    TYPE = 1

    def __init__(self, payload = None):
        if payload is None:
            payload = random.randint(0, sys.maxsize).to_bytes(4, byteorder='big')
        super().__init__(self.TYPE, payload)

    def respond_via(self, sock):
        resp = PongMessage(self._payload)
        resp.send_via(sock)
