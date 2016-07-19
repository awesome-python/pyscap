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

from scap.Model import Model
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Definition(Model):
    def from_xml(self, parent, el):
        super(Definition, self).from_xml(parent, el)

        self.id = el.attrib['id']

        self.criteria = None
        for child in el:
            if child.tag.endswith('criteria'):
                from scap.model.oval_defs_5.Criteria import Criteria
                c = Criteria()
                c.from_xml(self, child)
                self.criteria = c
        if self.criteria is None:
            logger.critical('No criteria found for definition ' + self.id)
            import sys
            sys.exit()
