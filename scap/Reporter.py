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

import logging
import xml.etree.ElementTree as ET
import uuid
import sys
import importlib

from scap.model.ai_1_1.ComputingDeviceType import ComputingDeviceType
from scap.model.ai_1_1.FQDNType import FQDNType
from scap.model.ai_1_1.ComputingDeviceHostnameType import ComputingDeviceHostnameType
from scap.model.ai_1_1.MotherboardGUIDType import MotherboardGUIDType
from scap.model.ai_1_1.ConnectionsType import ConnectionsType
from scap.model.ai_1_1.NetworkInterfaceType import NetworkInterfaceType
from scap.model.ai_1_1.IPAddressType import IPAddressType
from scap.model.ai_1_1.IPAddressIPv4Type import IPAddressIPv4Type
from scap.model.ai_1_1.IPAddressIPv6Type import IPAddressIPv6Type
from scap.model.ai_1_1.MACAddressType import MACAddressType
from scap.model.ai_1_1.ServiceType import ServiceType
from scap.model.ai_1_1.HostType import HostType
from scap.model.ai_1_1.ServicePortType import ServicePortType
from scap.model.ai_1_1.ProtocolType import ProtocolType
from scap.model.ai_1_1.CPEType import CPEType
from scap.model.ai_1_1.Source import Source
from scap.model.ai_1_1.Timestamp import Timestamp

from scap.model.arf_1_1.AssetReportCollectionElement import AssetReportCollectionElement
from scap.model.arf_1_1.ReportRequestsType import ReportRequestsType
from scap.model.arf_1_1.AssetsType import AssetsType
from scap.model.arf_1_1.ReportsType import ReportsType
from scap.model.arf_1_1.ReportRequestType import ReportRequestType
from scap.model.arf_1_1.AssetElement import AssetElement
from scap.model.arf_1_1.ReportType import ReportType
from scap.model.arf_1_1.RelationshipTypeEnumeration import RELATIONSHIP_TYPE_ENUMERATION

from scap.model.rep_core_1_1.RelationshipsType import RelationshipsType
from scap.model.rep_core_1_1.RelationshipType import RelationshipType
from scap.model.rep_core_1_1.RefElement import RefElement

logger = logging.getLogger(__name__)
class Reporter(object):
    @staticmethod
    def load(hosts, args, content):
        if content.tag == '{http://checklists.nist.gov/xccdf/1.1}Benchmark':
            from scap.reporter.xccdf_1_1.BenchmarkReporter import BenchmarkReporter
            return BenchmarkReporter(hosts, args, content)
        else:
            raise NotImplementedError('Reporting with ' + content.tag + ' content has not been implemented')

    def __init__(self, hosts, args, content):
        self.hosts = hosts
        self.content = content

    def report(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
