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
class Check(Simple):
    def __init__(self):
        super(Check, self).__init__()
        self.check_content_ref = None
        self.check_content_name = None
        self.ignore_attributes.extend([
            'selector',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}check-import',
            '{http://checklists.nist.gov/xccdf/1.2}check-export',
        ])

    def parse_attrib(self, name, value):
        if name == 'system':
            supported = [
                'http://oval.mitre.org/XMLSchema/oval-definitions-5',
                'http://scap.nist.gov/schema/ocil/2.0',
                'http://scap.nist.gov/schema/ocil/2',
            ]
            if value not in supported:
                raise NotImplementedError('Check system ' + value + ' is not implemented')
            else:
                self.system = value
        elif name == 'negate':
            self.negate = self.parse_boolean(value)
        elif name == 'multi-check':
            self.multi_check = self.parse_boolean(value)
        else:
            return super(Check, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}check-content-ref':
            self.check_content_ref = sub_el.attrib['href']
            if 'name' not in sub_el.attrib:
                logger.debug('Rule ' + self.parent.id + ' will load ' + self.check_content_ref + ' and use all items')
            else:
                self.check_content_name = sub_el.attrib['name']
                logger.debug('Rule ' + self.parent.id + ' will load ' + self.check_content_ref + ' and use item ' + self.check_content_name)
        else:
            return super(Check, self).parse_sub_el(sub_el)
        return True
