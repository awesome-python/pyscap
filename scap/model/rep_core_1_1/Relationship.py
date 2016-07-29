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
class Relationship(Model):
    class Scope(object):
        INCLUSIVE = 'inclusive'
        EXCLUSIVE = 'exclusive'

    def __init__(self, tag=None):
        super(Relationship, self).__init__(tag)

        self.refs = []

        self.type = None
        self.scope = Relationship.Scope.INCLUSIVE
        self.subject = None

        self.required_attributes.extend([
            'type',
            'subject',
        ])
        self.required_sub_elements.extend([
            '{' + self.get_xml_namespace() + '}ref',
        ])

    def get_attributes(self):
        attribs = super(Relationship, self).get_attributes()

        attribs['type'] = self.type
        attribs['scope'] = self.scope
        attribs['subject'] = self.subject

        return attribs

    def get_sub_elements(self):
        sub_els = super(Relationship, self).get_sub_elements()

        for ref in self.refs:
            sub_els.append(self.get_text_element('{' + self.get_xml_namespace() + '}ref', ref))

        return sub_els
