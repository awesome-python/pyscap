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

logger = logging.getLogger(__name__)
class Definition(Simple):
    def __init__(self):
        super(Definition, self).__init__()

        self.criteria = None

        self.tag_name = '{http://oval.mitre.org/XMLSchema/oval-definitions-5}definition'
        self.ignore_attributes.extend([
            'version',
            'class',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}metadata',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated definition ' + self.id)
        else:
            return super(Definition, self).parse_attribute(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}criteria':
            from scap.model.oval_defs_5.Criteria import Criteria
            c = Criteria()
            c.from_xml(self, sub_el)
            self.criteria = c
        else:
            return super(Definition, self).parse_sub_el(sub_el)
        return True

    def from_xml(self, parent, el):
        super(Definition, self).from_xml(parent, el)

        if self.criteria is None:
            logger.critical('No criteria found for definition ' + self.id)
            import sys
            sys.exit()
