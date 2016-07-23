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

from scap.model.Simple import Simple
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class OCIL(Simple):
    def __init__(self):
        super(OCIL, self).__init__()

        self.tag_name = '{http://scap.nist.gov/schema/ocil/2.0}ocil'
        self.ignore_sub_elements.extend([
            '{http://scap.nist.gov/schema/ocil/2.0}generator',
            '{http://scap.nist.gov/schema/ocil/2.0}document',
            '{http://scap.nist.gov/schema/ocil/2.0}questionnaires',
            '{http://scap.nist.gov/schema/ocil/2.0}test_actions',
            '{http://scap.nist.gov/schema/ocil/2.0}questions',
        ])

    def from_xml(self, parent, el):
        super(OCIL, self).from_xml(parent, el)
