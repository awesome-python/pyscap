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
    URI = 'http://scap.nist.gov/specifications/ai/vocabulary/relationships/1.0'
    
    #Term Domain Range Description
    HAS_TERMINATION_DEVICE = 'hasTerminationDevice' #ai:circuit ai:computing-device The circuit is terminated by the device.
    HAS_SERVICE_PROVIDER = 'hasServiceProvider' #ai:circuit ai:organization The circuit is owner/operated by the organization.
    #HAS_SERVICE_PROVIDER = 'hasServiceProvider' #ai:service ai:software The service is provided by the software.
    HAS_NETWORK_TERMINATION_POINT = 'hasNetworkTerminationPoint' #ai:circuit ai:network The circuit ends at the network.
    SERVED_BY = 'servedBy' #ai:database,ai:website ai:service The database or website is served up by the service.
    INSTALLED_ON_DEVICE = 'installedOnDevice' #ai:software ai:computing-device The software is installed on the computing device.
    CONNECTED_TO_NETWORK = 'connectedToNetwork' #ai:system ai:network The system is connected to the network.
    IS_OWNER_OF = 'isOwnerOf' #ai:person,ai:organization ai:it-asset The person or organization owns the IT asset.
    IS_ADMINISTRATOR_OF = 'isAdministratorOf' #ai:person ai:computing-device,ai:system The person is the system administrator of the computing device or system.
    PART_OF = 'partOf' #ai:person ai:organization The person is in some way a part of the organization.
    CONNECTED_TO = 'connectedTo' #ai:computing-device, ai:system ai:system The computing device or system is connected to the system.
