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

import datetime
import logging

from scap.model.xs.Simple import Simple

logger = logging.getLogger(__name__)
class Date(Simple):
    def parse_value(self, value):
        m = re.match(r'(-?\d\d\d\d)-(\d\d)-(\d\d)((([-+])(\d\d):(\d\d))|Z)?', value)
        if m:
            year, month, day, = m.group(1, 2, 3)
            if m.group(7) is not None and m.group(8) is not None:
                microsecond = m.group(8)
            else:
                microsecond = 0
            if m.group(4) is not None and m.group(4) == 'Z':
                tz = datetime.timezone.utc
            else:
                if m.group(5) is not None:
                    sign, hours, minutes = m.groups(6, 7, 8)
                    if sign == '-':
                        tz = datetime.timezone(- datetime.timedelta(hours=hours, minutes=minutes))
                    else:
                        tz = datetime.timezone(datetime.timedelta(hours=hours, minutes=minutes))
                else:
                    tz = datetime.timezone.utc

        self.value = datetime.datetime(year, month, day, hour, minute, second, microsecond, tz)
        return self.value
