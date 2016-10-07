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

from message.Message import Message

logger = logging.getLogger(__name__)
class ExceptionMessage(Message):
    def __init__(self, payload):
        if not isinstance(payload, dict) or 'exception' not in payload or 'traceback' not in payload:
            payload = {
                'exception': RuntimeError('Invalid payload for ExceptionMessage: ' + str(payload)),
                'traceback': '',
            }
        super().__init__(payload)

    def __str__(self):
        return self.__class__.__name__ + '[type=' + str(self.type) + \
            ', payload=' + str(self.payload['exception']) + ']\n' + \
            self.payload['traceback']
