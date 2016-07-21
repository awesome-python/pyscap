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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class RelationshipsContainer(Simple):
    def __init__(self):
        super(RelationshipsContainer, self).__init__()
        self.relationships = []

    # def get_attributes(self):
    #     attribs = super(RelationshipsContainer, self).get_attributes()
    #
    #     return attribs

    def get_sub_elements(self):
        sub_els = super(RelationshipsContainer, self).get_sub_elements()

        if len(self.relationships) > 0:
            relationships_el = ET.Element('{http://scap.nist.gov/schema/reporting-core/1.1}relationships')
            for relationship in self.relationships:
                relationships_el.append(relationship.to_xml())
            sub_els.append(relationships_el)

        return sub_els
