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

from scap.model.ai_1_1.ITAsset import ITAsset
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class ComputingDevice(ITAsset):
    def __init__(self):
        super(ComputingDevice, self).__init__()

        self.distinguished_name = None
        self.cpes = []
        self.connections = []
        self.fqdn = None
        self.hostname = None
        self.motherboard_guid = None

        self.tag_name = '{http://scap.nist.gov/schema/asset-identification/1.1}computing-device'

    def get_sub_elements(self):
        sub_els = super(ComputingDevice, self).get_sub_elements()

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
