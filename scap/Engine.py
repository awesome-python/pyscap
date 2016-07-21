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

import logging, inspect
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Engine(object):
    namespaces = {
        'ai_1_1': 'http://scap.nist.gov/schema/asset-identification/1.1',
        'arf_1_1': 'http://scap.nist.gov/schema/asset-reporting-format/1.1',
        'arf_rel_1_0': 'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0',
        'cpe_dict_2_0': 'http://cpe.mitre.org/dictionary/2.0',
        'cpe_lang_2_0': 'http://cpe.mitre.org/language/2.0',
        'dc_el_1_1': 'http://purl.org/dc/elements/1.1/',
        'ocil_2_0': 'http://scap.nist.gov/schema/ocil/2.0',
        'ocil_2': 'http://scap.nist.gov/schema/ocil/2',
        'oval_common_5': 'http://oval.mitre.org/XMLSchema/oval-common-5',
        'oval_defs_5': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
        'oval_defs_5_independent': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent',
        'oval_defs_5_windows': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'scap_1_2': 'http://scap.nist.gov/schema/scap/source/1.2',
        'rep_core_1_1': 'http://scap.nist.gov/schema/reporting-core/1.1',
        'xccdf_1_1': 'http://checklists.nist.gov/xccdf/1.1',
        'xccdf_1_2': 'http://checklists.nist.gov/xccdf/1.2',
        'xhtml': 'http://www.w3.org/1999/xhtml',
        'xlink': 'http://www.w3.org/1999/xlink',
        'xml_cat': 'urn:oasis:names:tc:entity:xmlns:xml:catalog',
        'xml_dsig_1_0': 'http://scap.nist.gov/schema/xml-dsig/1.0',
        'xml_schema_instance': 'http://www.w3.org/2001/XMLSchema-instance',
        'xmldsig_2000_09': 'http://www.w3.org/2000/09/xmldsig',
    }

    def __init__(self, content, hosts):
        self.hosts = hosts
        from scap.Model import Model
        self.content = Model.load(content)

    def collect(self, args):
        for host in self.hosts:
            host.connect()

            host.collect_facts()
            #TODO cache facts

            from scap.collector.ResultCollector import ResultCollector
            host.add_result_collector(ResultCollector.learn(host, self.content, args))
            host.collect_results()

            host.disconnect()

    def report(self):
        from scap.model.arf_1_1.AssetReportCollection import AssetReportCollection
        arc = AssetReportCollection()

        #TODO report requests

        for host in self.hosts:
            from scap.model.arf_1_1.Asset import Asset
            asset = Asset()
            asset.id = 'asset_' + host.facts['root_uuid']
            # TODO: fallback to mobo guid, eth0 mac address, eth0 ip address, hostname
            arc.assets.append(asset)

            from scap.model.ai_1_1.ComputingDevice import ComputingDevice
            comp = ComputingDevice()
            for cpe in host.facts['hw_cpe']:
                comp.cpes.append(cpe)
            comp.fqdn = host.facts['fqdn']
            comp.hostname = host.facts['hostname']
            try:
                comp.motherboard_guid = host.facts['hardware']['configuration']['uuid']
            except KeyError:
                logger.debug("Couldn't parse motherboard-guid")
            asset.asset = comp

            from scap.model.ai_1_1.Connection import Connection
            for c in host.facts['network_connections']:
                conn = Connection()
                conn.mac_address = c['mac_address']
                conn.ip_address = c['ip_address']
                conn.subnet_mask = c['subnet_mask']
                #TODO
                #conn.default_route = c['default_route']
                comp.connections.append(conn)

            # network services
            from scap.model.ai_1_1.Service import Service
            for svc in host.facts['network_services']:
                s = Service()
                s.host = svc['ip_address']
                s.port = svc['port']
                s.protocol = svc['protocol']

            from scap.model.arf_1_1.Report import Report
            import uuid
            report = Report()
            report.id = 'report_' + uuid.uuid4().hex
            arc.reports.append(report)

            from scap.model.rep_core_1_1.Relationship import Relationship
            rel = Relationship()
            rel.subject = report.id
            rel.type = 'isAbout'
            rel.refs.append(asset.id)
            arc.relationships.append(rel)

            # TODO createdFor relationship

        arc_et = ET.ElementTree(element=arc.to_xml())
        from StringIO import StringIO
        sio = StringIO()
        arc_et.write(sio, encoding='UTF-8', xml_declaration=True)
        sio.write("\n")
        return sio.getvalue()
