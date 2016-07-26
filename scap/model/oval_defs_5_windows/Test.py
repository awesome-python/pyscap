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

import scap.model.oval_defs_5.Test
import logging

logger = logging.getLogger(__name__)

class Test(scap.model.oval_defs_5.Test.Test):
    def __init__(self, tag_name=None):
        super(Test, self).__init__(tag_name)

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}object',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}state',
        ])
