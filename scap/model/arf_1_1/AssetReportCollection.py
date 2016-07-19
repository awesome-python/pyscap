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
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class AssetReportCollection(Model):
    def to_xml(self):
        arc = ET.ElementTree(element=ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset-report-collection'))
        root_el = arc.getroot()
        assets_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}assets')
        reports_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}reports')
        relationships_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/reporting-core/1.1}relationships')

        from StringIO import StringIO
        sio = StringIO()
        arc.write(sio, encoding='UTF-8', xml_declaration=True)
        sio.write("\n")
        return sio.getvalue()
