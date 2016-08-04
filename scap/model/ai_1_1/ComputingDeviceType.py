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
    TAG_MAP = {
        '{http://scap.nist.gov/schema/asset-identification/1.1}distinguished-name': {
            'class': 'scap.model.xs.Token',
            'attributes': {
                'source': {'class': 'SourceType'},
                'timestamp': {'class': 'TimestampType'},
            }
        },
        '{http://scap.nist.gov/schema/asset-identification/1.1}cpe': {'class': 'scap.model.xs.String'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}connections': {
            'class': 'scap.model.List',
            'items': {
                '{http://scap.nist.gov/schema/asset-identification/1.1}connection': {'class': 'NetworkInterfaceType'}
            }
        },
        '{http://scap.nist.gov/schema/asset-identification/1.1}fqdn': {'class': 'FQDNType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}hostname': {
            'class': 'HostnameType',
            'attributes': {
                'source': {'class': 'SourceType'},
                'timestamp': {'class': 'TimestampType'},
            }
        },
        '{http://scap.nist.gov/schema/asset-identification/1.1}motherboard-guid': {
            'class': 'scap.model.xs.String',
            'attributes': {
                'source': {'class': 'SourceType'},
                'timestamp': {'class': 'TimestampType'},
            }
        },
    }
    def __init__(self):
        super(ComputingDeviceType, self).__init__('{http://scap.nist.gov/schema/asset-identification/1.1}computing-device')    #

        self.distinguished_name = None
        self.cpes = []
        self.connections = []
        self.fqdn = None
        self.hostname = None
        self.motherboard_guid = None

    def get_sub_elements(self):
        sub_els = super(ComputingDeviceType, self).get_sub_elements()

        if self.distinguished_name is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}distinguished-name', self.distinguished_name))

        for cpe in self.cpes:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}cpe', cpe.to_fs_string()))

        if len(self.connections) > 0:
            sub_el = ET.Element('{http://scap.nist.gov/schema/asset-identification/1.1}connections')
            for conn in self.connections:
                sub_el.append(conn.to_xml())
            sub_els.append(sub_el)

        if self.fqdn is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}fqdn', self.fqdn))

        if self.hostname is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}hostname', self.hostname))

        if self.motherboard_guid is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}motherboard-guid', self.motherboard_guid))

        return sub_els
