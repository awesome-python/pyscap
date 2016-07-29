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
class TestResult(Model):
    # urn:xccdf:fact:asset:identifier:mac Ethernet media access control address (SHOULD be sent as a pair with the IPv4 or IPv6 address to ensure uniqueness)
    # urn:xccdf:fact:asset:identifier:ipv4 IPv4 address
    # urn:xccdf:fact:asset:identifier:ipv6 IPv6 address
    # urn:xccdf:fact:asset:identifier:host_name Host name of the asset, if assigned
    # urn:xccdf:fact:asset:identifier:fqdn Fully qualified domain name
    # urn:xccdf:fact:asset:identifier:ein Equipment identification number or other inventory tag number
    # urn:xccdf:fact:asset:identifier:pki: X.509 PKI certificate for the asset (encoded in Base-64)
    # urn:xccdf:fact:asset:identifier:pki:thumbprint SHA-1 hash of the PKI certification for the asset (encoded in Base-64)
    # urn:xccdf:fact:asset:identifier:guid Globally unique identifier for the asset
    # urn:xccdf:fact:asset:identifier:ldap LDAP directory string (distinguished name) of the asset, if assigned
    # urn:xccdf:fact:asset:identifier:active_directory Active Directory realm to which the asset belongs, if assigned
    # urn:xccdf:fact:asset:identifier:nis_domain NIS domain of the asset, if assigned
    # urn:xccdf:fact:asset:environmental_information: owning_organization Organization that tracks the asset on its inventory
    # urn:xccdf:fact:asset:environmental_information: current_region Geographic region where the asset is located
    # urn:xccdf:fact:asset:environmental_information: administration_unit Name of the organization that does system administration for the asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:title Title (e.g., Mr, Ms, Col) of the system administrator for an asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:e-mail E-mail address of the system administrator for the asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:first_name First name of the system administrator for the asset
    # urn:xccdf:fact:asset:environmental_information: administration_poc:last_name Last name of the system administrator for the asset
    pass
