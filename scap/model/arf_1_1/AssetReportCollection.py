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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class AssetReportCollection(Simple):
    def __init__(self):
        self.report_requests = []
        self.assets = []
        self.reports = []
        self.relationships = []
        self.extended_infos = []

    def to_xml(self):
        arc_et = ET.ElementTree(element=ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset-report-collection'))
        root_el = arc_et.getroot()

        if len(self.report_requests) > 0:
            report_requests_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}report-requests')
            for report_request in self.report_requests:
                report_requests_el.append(report_request.to_xml())

        if len(self.assets) > 0:
            assets_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}assets')
            for asset in self.assets:
                assets_el.append(asset.to_xml())

        reports_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}reports')
        for report in self.reports:
            reports_el.append(report.to_xml())

        if len(self.relationships) > 0:
            relationships_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/reporting-core/1.1}relationships')
            for relationship in self.relationships:
                relationships_el.append(relationship.to_xml())

        if len(self.extended_infos) > 0:
            extended_infos_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/reporting-core/1.1}extended-infos')
            for extended_info in self.extended_infos:
                extended_infos_el.append(extended_info.to_xml())

        from StringIO import StringIO
        sio = StringIO()
        arc.write(sio, encoding='UTF-8', xml_declaration=True)
        sio.write("\n")
        return sio.getvalue()
