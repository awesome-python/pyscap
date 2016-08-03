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
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class ReportRequestType(Model):
    def __init__(self):
        super(ReportRequestType, self).__init__('{http://scap.nist.gov/schema/asset-reporting-format/1.1}report-request')    #

        self.content = None
        self.remote_resource = None

        self.required_attributes.append('id')

    def get_sub_elements(self):
        sub_els = super(ReportRequestType, self).get_sub_elements()

        if self.content is not None:
            sub_el = ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}content')
            sub_el.append(self.content)
            sub_els.append(sub_el)
        elif self.remote_resource is not None:
            sub_els.append(self.remote_resource.to_xml())
        else:
            logger.critical('report_request must define content or remote-resource')
            import sys
            sys.exit()

        return sub_els
