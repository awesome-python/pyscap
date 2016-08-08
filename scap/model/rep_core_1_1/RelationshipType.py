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
class RelationshipType(Model):
    'attributes': {
        'type': {'required': True}
        'subject': {'required': True}
    }
    def __init__(self, tag=None):
        super(RelationshipType, self).__init__(tag)

        self.refs = []

        self.type = None
        self.scope = 'inclusive'
        self.subject = None

    def get_attributes(self):
        attribs = super(RelationshipType, self).get_attributes()

        attribs['type'] = self.type
        attribs['scope'] = self.scope
        attribs['subject'] = self.subject

        return attribs

    def get_sub_elements(self):
        sub_els = super(RelationshipType, self).get_sub_elements()

        for ref in self.refs:
            sub_els.append(self.get_text_element('{' + self.get_xml_namespace() + '}ref', ref))

        return sub_els
