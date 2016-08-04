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
class AssetType(Model):
    ATTRIBUTE_MAP = {
        'timestamp': {'class': 'TimestampType'}
    }
    TAG_MAP = {
        '{http://scap.nist.gov/schema/asset-identification/1.1}synthetic-id': {'class': 'SyntheticIDType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}location-point': {'class': 'LocationPointType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}location-region': {'class': 'LocationRegionType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}extended-information': {'class': 'ExtendedInformationType'},
    }

    # abstract
    def __init__(self, tag=None):
        super(AssetType, self).__init__(tag)

        self.synthetic_ids = []
        self.locations = []
        self.extended_information = []

    def get_sub_elements(self):
        sub_els = super(AssetType, self).get_sub_elements()

        for sid in self.synthetic_ids:
            sub_els.append(sid.to_xml())

        for loc in self.locations:
            sub_els.append(loc.to_xml())

        for ext in self.extended_information:
            ei = ET.Element('{http://scap.nist.gov/schema/asset-identification/1.1}extended-information')
            ei.append(ext.to_xml())
            sub_els.append(ei)

        return sub_els
