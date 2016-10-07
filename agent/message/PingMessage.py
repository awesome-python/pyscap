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
import os
import sys

from message.Message import Message
from message.PongMessage import PongMessage

logger = logging.getLogger(__name__)
class PingMessage(Message):
    def __init__(self, payload = None):
        if payload is None:
            try:
                payload = os.urandom(4)
            except:
            # avoid pulling in random lib; most OSs support os.urandom
            #     import random
            #     random.seed()
            #     payload = random.randint(0, sys.maxsize)
            # else:
                payload = Message.MAGIC
        super().__init__(payload)

    def respond_via(self, sock):
        resp = PongMessage(self.payload)
        resp.send_via(sock)
