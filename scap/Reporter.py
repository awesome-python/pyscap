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

from scap.model.ai_1_1.ComputingDeviceType import ComputingDeviceType
from scap.model.ai_1_1.FQDNType import FQDNType
from scap.model.ai_1_1.ComputingDeviceHostnameType import ComputingDeviceHostnameType
from scap.model.ai_1_1.MotherboardGUIDType import MotherboardGUIDType
from scap.model.ai_1_1.ConnectionsType import ConnectionsType
from scap.model.ai_1_1.NetworkInterfaceType import NetworkInterfaceType
from scap.model.ai_1_1.IPAddressType import IPAddressType
from scap.model.ai_1_1.MACAddressType import MACAddressType
from scap.model.ai_1_1.ServiceType import ServiceType
from scap.model.ai_1_1.HostType import HostType
from scap.model.ai_1_1.ServicePortType import ServicePortType
from scap.model.ai_1_1.ProtocolType import ProtocolType
from scap.model.ai_1_1.CPEType import CPEType

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
    def __init__(self, content, hosts):
        self.hosts = hosts
        self.content = content

    def report(self):
        arc = AssetReportCollectionElement()

        arc.relationships = RelationshipsType()
        arc.report_requests = ReportRequestsType()
        arc.assets = AssetsType()
        arc.reports = ReportsType()

        # TODO arc.extended-infos

        report_request = ReportRequestType()
        arc.report_requests.report_requests.append(report_request)

        report_request.id = 'report-request_' + uuid.uuid4().hex

        #report_request.content = self.content.to_xml()
        report_request.content = ET.Element('stuff')

        for host in self.hosts:
            asset = AssetElement()
            arc.assets.assets.append(asset)

            asset.id = 'asset_' + host.facts['system_uuid']

            comp = ComputingDeviceType()
            asset.assets.append(comp)

            # TODO: if root_uuid is unavailable
            # TODO: fallback to mobo guid, eth0 mac address, eth0 ip address, hostname

            for cpe in host.facts['cpe']:
                c = CPEType()
                c.value = cpe.to_uri_string()
                comp.cpes.append(c)

            comp.fqdn = FQDNType()
            # TODO multiple FQDNs
            comp.fqdn.value = host.facts['fqdn'][0]

            comp.hostname = ComputingDeviceHostnameType()
            comp.hostname.value = host.facts['hostname']

            try:
                comp.motherboard_guid = MotherboardGUIDType()
                comp.motherboard_guid.value = host.facts['system_uuid']
            except KeyError:
                logger.debug("Couldn't parse motherboard-guid")

            comp.connections = ConnectionsType()

            for dev, net_con in host.facts['network_connections'].items():
                logger.debug('Producing Connection for device ' + dev)
                for address in net_con['network_addresses']:
                    conn = NetworkInterfaceType()
                    comp.connections.connections.append(conn)

                    conn.mac_address = MACAddressType()
                    conn.mac_address.value = host.facts['network_connections'][dev]['mac_address']

                    conn.ip_address = IPAddressType()
                    conn.ip_address.value = address['address']

                    conn.subnet_mask = IPAddressType()
                    conn.subnet_mask.value = address['subnet_mask']

                    if 'default_route' in host.facts['network_connections'][dev]:
                        conn.default_route = IPAddressType()
                        conn.default_route.value = host.facts['network_connections'][dev]['default_route']

            # network services
            for svc in host.facts['network_services']:
                s = ServiceType()
                asset.assets.append(s)

                s.host = HostType()

                s.host.fqdn = FQDNType()
                # TODO multiple FQDNs
                s.host.fqdn.value = host.facts['fqdn'][0]

                s.host.ip_address = IPAddressType()
                s.host.ip_address.value = svc['ip_address']

                port = ServicePortType()
                port.value = svc['port']
                # TODO port.source
                # TODO port.timestamp
                s.ports.append(port)

                s.protocol = ProtocolType()
                s.protocol.value = svc['protocol']

            report = ReportType()
            arc.reports.reports.append(report)

            report.id = 'report_' + uuid.uuid4().hex

            rel = RelationshipType()
            arc.relationships.relationships.append(rel)
            rel.subject = report.id
            rel.type = 'isAbout'
            ref = RefElement()
            ref.value = asset.id
            rel.refs.append(ref)

            # TODO 'retrievedFrom' relationship
            # TODO 'createdBy' relationship
            # TODO 'hasSource' relationship
            # TODO 'recordedBy' relationship
            # TODO 'initiatedBy' relationship

            rel = RelationshipType()
            arc.relationships.relationships.append(rel)
            rel.subject = report.id
            rel.type = 'createdFor'
            ref = RefElement()
            ref.value = report_request.id
            rel.refs.append(ref)

            # TODO 'hasMetadata' relationship

        arc_et = ET.ElementTree(element=arc.to_xml())
        return arc_et
