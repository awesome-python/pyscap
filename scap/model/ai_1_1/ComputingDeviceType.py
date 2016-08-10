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

from scap.model.ai_1_1.ITAssetType import ITAssetType
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class ComputingDeviceType(ITAssetType):
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/asset-identification/1.1',
        'tag_name': 'computing-device',
        'elements': {
            '{http://scap.nist.gov/schema/asset-identification/1.1}distinguished-name': {'class': 'DistinguishedNameType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}cpe': {'append': 'cpes', 'class': 'CPEType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}connections': {
                'list': 'connections',
                'classes': {
                    '{http://scap.nist.gov/schema/asset-identification/1.1}connection': 'NetworkInterfaceType',
                },
            },
            '{http://scap.nist.gov/schema/asset-identification/1.1}fqdn': {'class': 'FQDNType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}hostname': {'class': 'ComputingDeviceHostnameType'},
            '{http://scap.nist.gov/schema/asset-identification/1.1}motherboard-guid': {'class': 'MotherboardGUIDType'},
        },
    }
    #TODO: cpes as fs_string
