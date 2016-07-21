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

class RelationshipTypes(object):
    URI = 'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0'

    #Term Domain Range Description
    IS_ABOUT = 'isAbout' #arf:report ai:asset The data in the report is about the asset.
    RETRIEVED_FROM = 'retrievedFrom' #arf:report ai:asset The data in the report was retrieved from the asset. This relationship will generally be used when the asset identifies some data store that houses information. This relationship indicates that the data came from the asset, but the asset did not create, or in any other way produce, the data, other than to supply the stored data.
    CREATED_BY = 'createdBy' #arf:report ai:asset The data in the report was created by the asset. This relationship SHOULD refer to the tool that created the content originally.
    HAS_SOURCE = 'hasSource' #arf:report ai:asset The report contains knowledge from the asset. This relationship refers to the asset that supplied the knowledge to create the report content. This relationship implies that the asset is authoritative about the information.
    RECORDED_BY = 'recordedBy' #arf:report ai:asset The information in the report was recorded by the asset. This relationship will usually be used when the report content is data about a digital event that is captured by an asset (e.g., a piece of software fires a digital event).
    INITIATED_BY = 'initiatedBy' #arf:report ai:asset The information in the report was initiated by the asset. This relationship will usually be used when the report content represents a digital event and that digital event is initiated by the asset.
    CREATED_FOR = 'createdFor' #arf:report ai:report-request The report was created because of the report request. This relationship will usually be used to associate request and response type data.
    HAS_METADATA = 'hasMetadata' #arf:report ai:report The subject report has additional metadata that is represented in the object report.
