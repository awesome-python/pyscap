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

from scap.model.ai_1_1.AssetType import AssetType
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class OrganizationType(AssetType):
    TAG_MAP = {
        '{xnl}:OrganisationNameDetails': {},
        '{http://scap.nist.gov/schema/asset-identification/1.1}email-address': {'class': 'EmailAddressType'},
        '{http://scap.nist.gov/schema/asset-identification/1.1}cidr': {
            'class': 'CIDRType',
            'attributes': {
                'source': {'class': 'SourceType'},
                'timestamp': {'class': 'TimestampType'},
            }
        },
    }
    def __init__(self):
        super(OrganizationType, self).__init__('{http://scap.nist.gov/schema/asset-identification/1.1}organization')    #

        self.email_addresses = []
        self.telephone_numbers = []
        self.website_urls = []

        self.name_details = []
