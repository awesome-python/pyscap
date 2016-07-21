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

from scap.model.rep_core_1_1.RelationshipsContainer import RelationshipsContainer
import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)
class AssetReportCollection(RelationshipsContainer):
    def __init__(self):
        super(AssetReportCollection, self).__init__()
        self.report_requests = []
        self.assets = []
        self.reports = []
        self.extended_infos = []

    def get_tag(self):
        return '{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset-report-collection'

    def get_sub_elements(self):
        sub_els = []

        if len(self.report_requests) > 0:
            report_requests_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}report-requests')
            for report_request in self.report_requests:
                report_requests_el.append(report_request.to_xml())
            sub_els.append(report_requests_el)

        if len(self.assets) > 0:
            assets_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}assets')
            for asset in self.assets:
                assets_el.append(asset.to_xml())
            sub_els.append(assets_el)

        reports_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}reports')
        for report in self.reports:
            reports_el.append(report.to_xml())
        sub_els.append(reports_el)

        if len(self.extended_infos) > 0:
            extended_infos_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}extended-infos')
            for extended_info in self.extended_infos:
                ei = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}extended-info')
                ei.append(extended_info.to_xml())
                sub_els.append(ei)
                extended_infos_el.append(ei.to_xml())
            sub_els.append(extended_infos_el)

        # want the relationships from superclass to come at the end
        sub_els.extend(super(AssetReportCollection, self).get_sub_elements())

        return sub_els
