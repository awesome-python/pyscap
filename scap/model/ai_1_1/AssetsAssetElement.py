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
class AssetsAssetElement(Model):
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/asset-identification/1.1',
        'tag_name': 'asset',
        'elements': {
            '{http://scap.nist.gov/schema/asset-identification/1.1}circuit': {'in': 'asset', 'class': 'CircuitType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}computing-device': {'in': 'asset', 'class': 'ComputingDeviceType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}data': {'in': 'asset', 'class': 'DataType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}database': {'in': 'asset', 'class': 'DatabaseType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}network': {'in': 'asset', 'class': 'NetworkType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}organization': {'in': 'asset', 'class': 'OrganizationType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}person': {'in': 'asset', 'class': 'PersonType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}service': {'in': 'asset', 'class': 'ServiceType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}software': {'in': 'asset', 'class': 'SoftwareType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}system': {'in': 'asset', 'class': 'SystemType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}website': {'in': 'asset', 'class': 'WebsiteType'},
        },
        'attributes': {
            'id': {'type': 'NCName', 'required': True},
            '*': {'ignore': True},
        }
    }
