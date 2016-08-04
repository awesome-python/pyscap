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

from scap.model.rep_core_1_1.RelationshipsContainerType import RelationshipsContainerType
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class AssetsType(RelationshipsContainerType):
    TAG_MAP = {
        '{http://scap.nist.gov/schema/asset-identification/1.1}circuit': {'class': 'CircuitType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}computing-device': {'class': 'ComputingDeviceType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}data': {'class': 'DataType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}database': {'class': 'DatabaseType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}network': {'class': 'NetworkType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}organization': {'class': 'OrganizationType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}person': {'class': 'PersonType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}service': {'class': 'ServiceType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}software': {'class': 'SoftwareType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}system': {'class': 'SystemType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}website': {'class': 'WebsiteType'},
    }
    def __init__(self):
        super(AssetsType, self).__init__('{http://scap.nist.gov/schema/asset-identification/1.1}assets')

        self.assets = []
