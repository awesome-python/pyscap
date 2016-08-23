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

class ColorFormatter(logging.Formatter):
    FG_BLACK, FG_RED, FG_GREEN, FG_YELLOW, FG_BLUE, FG_MAGENTA, FG_CYAN, FG_WHITE = list(range(30, 38))
    BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE = list(range(40, 48))
    BOLD, ITALIC, UNDERLINE, STRIKETHROUGH = (1, 3, 4, 9)

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[%sm"    # bold
    BOLD_SEQ = "\033[1m"

    COLORS = {
        'CRITICAL': [FG_WHITE, BG_RED, BOLD],
        'ERROR': [FG_RED, BOLD],
        'WARNING': [FG_YELLOW, BOLD],
        'INFO': [FG_WHITE, BOLD],
        'DEBUG': [FG_BLUE, BOLD],
    }
    def format(self, record):
        levelname = record.levelname
        if levelname in self.COLORS:
            levelname_color = self.COLOR_SEQ % ';'.join(map(str, self.COLORS[levelname])) + levelname + self.RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)
