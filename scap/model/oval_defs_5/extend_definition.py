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
class extend_definition(Model):
    def __init__(self):
        super(extend_definition, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}extend_definition

        self.applicability_check = False
        self.definition_ref = None
        self.negate = False

        self.ignore_attributes.extend([
            'comment',
        ])

    def parse_attribute(self, name, value):
        if name == 'applicability_check':
            self.applicability_check = self.parse_boolean(value)
        elif name == 'definition_ref':
            self.definition_ref = value
        elif name == 'negate':
            self.negate = self.parse_boolean(value)
        else:
            return super(extend_definition, self).parse_attribute(name, value)
        return True

    def from_xml(self, parent, el):
        super(extend_definition, self).from_xml(parent, el)

        if self.definition_ref is None:
            logger.critical('definition_ref not defined in extend_definition')
            import sys
            sys.exit()
