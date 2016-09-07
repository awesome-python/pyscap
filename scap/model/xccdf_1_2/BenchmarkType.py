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

logger = logging.getLogger(__name__)
class BenchmarkType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}status': {'append': 'statuses', 'class': 'StatusType', 'min': 1, 'max': None, 'ignore': True},
            '{http://purl.org/dc/elements/1.1/}dc-status': {'append': 'dc_statuses', 'class': 'DCStatusType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}title': {'append': 'titles', 'class': 'TextType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}description': {'append': 'descriptions', 'class': 'HTMLTextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}notice': {'map': 'notices', 'class': 'NoticeType', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.2}front-matter': {'append': 'front_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}rear-matter': {'append': 'rear_matter', 'class': 'HtmlTextWithSubType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}reference': {'append': 'references', 'class': 'ReferenceType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}plain-text': {'append': 'plain_texts', 'class': 'PlainTextType', 'min': 0, 'max': None, 'ignore': True},
            '{http://cpe.mitre.org/language/2.0}platform-specification': {'class': 'scap.model.cpe_2_3.PlatformSpecificationType', 'min': 0, 'max': 1, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}platform': {'class': 'CPE2IDRefType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}version': {'class': 'VersionType', 'min': 1, 'max': 1, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}metadata': {'append': 'metadata', 'class': 'MetadataType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}model': {'append': 'models', 'class': 'ModelType', 'min': 0, 'max': None, 'ignore': True},
            '{http://checklists.nist.gov/xccdf/1.2}Profile': {'class': 'ProfileType', 'min': 0, 'max': None, 'map': 'profiles'},
            '{http://checklists.nist.gov/xccdf/1.2}Value': {'class': 'ValueType', 'min': 0, 'max': None, 'map': 'values'},
            '{http://checklists.nist.gov/xccdf/1.2}Group': {'class': 'GroupType', 'min': 0, 'max': None, 'map': 'groups'},
            '{http://checklists.nist.gov/xccdf/1.2}Rule': {'class': 'RuleType', 'min': 0, 'max': None, 'map': 'rules'},
            '{http://checklists.nist.gov/xccdf/1.2}TestResult': {'class': 'TestResultType', 'min': 0, 'max': None, 'map': 'tests'},
            '{http://checklists.nist.gov/xccdf/1.2}signature': {'class': 'SignatureType', 'min': 0, 'max': 1, 'ignore': True},
        },
        'attributes': {
            'id': {'required': True, 'type': 'BenchmarkIDPattern'},
            'Id': {'ignore': True, 'type': 'ID'},
            'resolved': {'ignore': True, 'type': 'Boolean', 'default': False},
            'style': {'ignore': True, 'type': 'String'},
            'style-href': {'ignore': True, 'type': 'AnyURI'},
        },
    }

    def from_xml(self, parent, el):
        super(BenchmarkType, self).from_xml(parent, el)

        for notice in list(self.notices.values()):
            logger.info('Notice: \n' + notice.value)

        for profile_id in self.profiles:
            logger.debug('found profile ' + profile_id)
