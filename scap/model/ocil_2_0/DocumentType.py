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

logger = logging.getLogger(__name__)
class DocumentType(Model):
    def __init__(self):
        super(DocumentType, self).__init__()

        self.title = None
        self.descriptions = []
        self.notices = []

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}title':
            self.title = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}description':
            self.descriptions = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}notice':
            self.notices = sub_el.text
        else:
            return super(DocumentType, self).parse_sub_el(sub_el)
        return True
