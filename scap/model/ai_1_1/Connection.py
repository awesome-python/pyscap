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

from scap.model.ai_1_1.AI import AI
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Connection(AI):
    def __init__(self):
        super(Connection, self).__init__()    # {http://scap.nist.gov/schema/asset-identification/1.1}connection

        self.ip_address = None
        self.mac_address = None
        self.urls = []
        self.subnet_mask = None
        self.default_route = None

    def get_sub_elements(self):
        sub_els = super(Connection, self).get_sub_elements()

        if self.ip_address is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}ip-address', self.ip_address))

        if self.mac_address is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}mac-address', self.mac_address))

        for url in self.urls:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}url', url))

        if self.subnet_mask is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}subnet-mask', self.subnet_mask))

        if self.default_route is not None:
            sub_els.append(self.get_text_element('{http://scap.nist.gov/schema/asset-identification/1.1}default-route', self.default_route))

        return sub_els
