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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class RelationshipsContainerType(Model):
    def __init__(self, tag=None):
        super(RelationshipsContainerType, self).__init__(tag)
        self.relationships = []

    def get_sub_elements(self):
        sub_els = super(RelationshipsContainerType, self).get_sub_elements()

        if len(self.relationships) > 0:
            relationships_el = ET.Element('{' + self.get_xml_namespace() + '}relationships')
            for relationship in self.relationships:
                relationships_el.append(relationship.to_xml())
            sub_els.append(relationships_el)

        return sub_els
