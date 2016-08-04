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
class ServiceType(ITAssetType):
    def __init__(self):
        super(ServiceType, self).__init__('{http://scap.nist.gov/schema/asset-identification/1.1}service')    #

        self.host = None
        self.ports = []
        self.port_ranges = []
        self.protocol = None

    def get_sub_elements(self):
        sub_els = super(ServiceType, self).get_sub_elements()

        if self.host is not None:
            sub_els.append(self.host.to_xml())

        for port in self.ports:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}port', port))

        for port_range in self.port_ranges:
            sub_els.append(port_range.to_xml())

        if self.protocol is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}protocol', self.protocol))
        return sub_els
