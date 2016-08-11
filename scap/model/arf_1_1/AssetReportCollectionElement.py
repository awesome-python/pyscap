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
import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)
class AssetReportCollectionElement(RelationshipsContainerType):
    MODEL_MAP = {
        'xml_namespace': 'http://scap.nist.gov/schema/asset-reporting-format/1.1',
        'tag_name': 'asset-report-collection',
        'elements': {
            '{http://scap.nist.gov/schema/asset-reporting-format/1.1}report-requests': {
                'list': 'report_requests',
                'classes': {
                    '{http://scap.nist.gov/schema/asset-reporting-format/1.1}report-request': 'ReportRequestType',
                }
            },
            '{http://scap.nist.gov/schema/asset-reporting-format/1.1}assets': {
                'list': 'assets',
                'classes': {
                    '{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset': 'AssetElement',
                }
            },
            '{http://scap.nist.gov/schema/asset-reporting-format/1.1}reports': {
                'list': 'reports',
                'classes': {
                    '{http://scap.nist.gov/schema/asset-reporting-format/1.1}report': 'ReportType',
                }
            },
            '{http://scap.nist.gov/schema/asset-reporting-format/1.1}extended-infos': {
                'list': 'extended_infos',
                'classes': {
                    '{http://scap.nist.gov/schema/asset-reporting-format/1.1}extended-info': 'ExtendedInfoElement',
                }
            },
        },
        'attributes': {
            'id': {'type': 'NCName', 'required': True},
            '*': {'ignore': True},
        }
    }
