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
        self.check_content = None
        self.ignore_attributes.extend(['selector'])
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
            content_el = self.resolve_reference(sub_el.attrib['href'])
            if not content_el.tag.startswith('{' + self.system):
                raise RuntimeError('Check system does not match loaded reference')
            if self.system == Engine.namespaces['oval_defs_5']:
                from scap.model.oval_defs_5.OVALDefinitions import OVALDefinitions
                self.check_content = OVALDefinitions()
                self.check_content.from_xml(self, content_el)
                # TODO need to specify def name
            elif self.system == Engine.namespaces['ocil_2_0'] or self.system == Engine.namespaces['ocil_2']:
                from scap.model.ocil_2_0.OCIL import OCIL
                self.check_content = OCIL()
                self.check_content.from_xml(self, content_el)
                # TODO need to specify using name
            else:
                raise RuntimeError('Unknown check content type: ' + self.system)
        else:
            return super(Check, self).parse_sub_el(sub_el)
        return True

    def from_xml(self, parent, el):
        super(Check, self).from_xml(parent, el)
        if self.check_content is None:
            logger.critical('Check for rule ' + parent.id + ' could not be loaded')
            import sys
            sys.exit()
