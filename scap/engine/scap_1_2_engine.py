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

import logging, sys, urlparse
import xml.etree.ElementTree as ET
import scap.engine.engine

logger = logging.getLogger(__name__)
class SCAP1_2Engine(scap.engine.engine.Engine):
    def __init__(self, content, args, hosts):
        self.content = content
        self.hosts = hosts

        root = content.getroot()
        # find the specified data stream or the only data stream if none specified
        data_streams = {}
        for ds in root.findall("./scap_1_2:data-stream", SCAP1_2Engine.namespaces):
            data_streams[ds.attrib['id']] = ds

        if 'data_stream' in args:
            if args['data_stream'] not in data_streams:
                logger.critical('Specified --data_stream, ' + args['data_stream'] + ', not found in content. Available data streams: ' + str(data_streams.keys()))
                sys.exit()
            else:
                self.data_stream = data_streams[args['data_stream']]
        else:
            if len(data_streams) == 1:
                self.data_stream = data_streams.values()[0]
            else:
                logger.critical('No --data_stream specified and unable to implicitly choose one. Available data-streams: ' + str(data_streams.keys()))
                sys.exit()
        logger.info('Using data stream ' + self.data_stream.attrib['id'])

        checklist_ids = []
        xpath = "./scap_1_2:checklists"
        xpath += "/scap_1_2:component-ref"
        for c in self.data_stream.findall(xpath, SCAP1_2Engine.namespaces):
            checklist_ids.append(c.attrib['{' + SCAP1_2Engine.namespaces['xlink'] + '}href'][1:])
        if 'checklist' in args:
            if args['checklist'] not in checklist_ids:
                logger.critical('Specified --checklist, ' + args['checklist'] + ', not found in content. Available checklists: ' + str(checklist_ids))
                sys.exit()
            else:
                checklist_id = args['checklist']
        else:
            if len(checklist_ids) == 1:
                checklist_id = checklist_ids[0]
            else:
                logger.critical('No --checklist specified and unable to implicitly choose one. Available checklists: ' + str(checklist_ids))
                sys.exit()
        self.checklist = root.find("./scap_1_2:component[@id='" + checklist_id + "']", SCAP1_2Engine.namespaces)
        logger.info('Using checklist ' + self.checklist.attrib['id'])

        profiles = {}
        xpath = "./xccdf_1_2:Benchmark"
        xpath += "/xccdf_1_2:Profile"
        for p in self.checklist.findall(xpath, SCAP1_2Engine.namespaces):
            profiles[p.attrib['id']] = p
        if 'profile' in args:
            if args['profile'] not in profiles:
                logger.critical('Specified --profile, ' + args['profile'] + ', not found in content. Available profiles: ' + str(profiles.keys()))
                sys.exit()
            else:
                self.profile = profiles[args['data_stream']]
        else:
            if len(profiles) == 1:
                self.profile = profiles.values()[0]
            else:
                logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(profiles.keys()))
                sys.exit()
        if 'extends' in self.profile.attrib:
            logger.critical('Profiles with @extends are not supported')
            sys.exit()
        logger.info('Using profile ' + self.profile.attrib['id'])

        self.rules = {}
        xpath = ".//xccdf_1_2:Rule"
        for r in self.checklist.findall(xpath, SCAP1_2Engine.namespaces):
            xpath = "./xccdf_1_2:select[@idref='" + r.attrib['id'] + "']"
            s = self.profile.find(xpath, SCAP1_2Engine.namespaces)
            if s is not None:
                if s.attrib['selected'] == 'true':
                    logger.info('Rule selected by profile: ' + r.attrib['id'])
                    self.rules[r.attrib['id']] = r
            else:
                if r.attrib['selected'] == 'true':
                    logger.info('Rule selected by default: ' + r.attrib['id'])
                    self.rules[r.attrib['id']] = r

        self.values = {}
        xpath = ".//xccdf_1_2:Value"
        for v in self.checklist.findall(xpath, SCAP1_2Engine.namespaces):
            v_id = v.attrib['id']
            logger.debug('Collecting value ' + v_id)
            self.values[v_id] = { 'element': v }
            selectors = {}
            for vs in v.findall('xccdf_1_2:value', SCAP1_2Engine.namespaces):
                if 'selector' in vs.attrib:
                    logger.debug('Selector value of ' + v_id + ' ' + vs.attrib['selector'] + ' = ' + str(vs.text))
                    selectors[vs.attrib['selector']] = vs.text
                else:
                    logger.debug('Default value of ' + v_id + ' is ' + str(vs.text))
                    self.values[v_id]['value'] = vs.text
            xpath = "./xccdf_1_2:refine-value[@idref='" + v_id + "']"
            rv = self.profile.find(xpath, SCAP1_2Engine.namespaces)
            if rv is not None:
                logger.info('Modifying value ' + v_id + ' by profile ' + self.profile.attrib['id'] + ' using selector ' + rv.attrib['selector'])
                self.values[v_id]['value'] = selectors[rv.attrib['selector']]
            logger.info('Using ' + v.attrib['type'] + ' ' + v.attrib['operator'] + ' ' + str(self.values[v_id]['value']) + ' for value ' + v_id)

    def collect(self):
        for host in self.hosts:
            host.connect()
            host.collect_facts()

            #for rule_id in self.rules:
                #host.test_rule(self.rules[rule_id], self.values, self.content)
            host.disconnect()

    def report(self):
        arc = ET.ElementTree(element=ET.Element('{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset-report-collection'))
        root_el = arc.getroot()
        assets_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}assets')
        reports_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}reports')
        relationships_el = ET.SubElement(root_el, '{http://scap.nist.gov/schema/reporting-core/1.1}relationships')

        for host in self.hosts:
            asset_el = ET.SubElement(assets_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}asset')
            asset_id = 'asset_' + host.facts['root_uuid']
            # TODO: fallback to mobo guid, eth0 mac address, eth0 ip address, hostname
            asset_el.attrib['id'] = asset_id

            ai = ET.SubElement(asset_el, '{http://scap.nist.gov/schema/asset-identification/1.1}computing-device')
            # motherboard should be the first discovered hardware cpe
            ai.attrib['cpe'] = host.facts['hw_cpe'][0].to_uri_string()
            ai.attrib['default-route'] = host.facts['default_route']
            ai.attrib['fqdn'] = host.facts['fqdn']
            ai.attrib['hostname'] = host.facts['hostname']
            try:
                ai.attrib['motherboard-guid'] = host.facts['hardware']['configuration']['uuid']
            except KeyError:
                logger.debug("Couldn't parse motherboard-guid")
            conns = ET.SubElement(ai, '{http://scap.nist.gov/schema/asset-identification/1.1}connections')
            for c in host.facts['network_connections']:
                conn = ET.SubElement(conns, '{http://scap.nist.gov/schema/asset-identification/1.1}connection')
                # mac-address
                conn.attrib['mac-address'] = c['mac_address']
                # ip-address
                conn.attrib['ip-address'] = c['ip_address']
                # subnet-mask
                conn.attrib['subnet-mask'] = c['subnet_mask']

            # network services
            for svc in host.facts['network_services']:
                ai = ET.SubElement(asset_el, '{http://scap.nist.gov/schema/asset-identification/1.1}service')
                ai.attrib['host'] = svc['ip_address']
                ai.attrib['port'] = svc['port']
                ai.attrib['protocol'] = svc['protocol']

            report_el = ET.SubElement(reports_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}report')
            import uuid
            report_id = 'report_' + uuid.uuid4().hex
            report_el.attrib['id'] = report_id

            # TODO embed content

            relationships = []
            rel_el = ET.SubElement(relationships_el, '{http://scap.nist.gov/schema/asset-reporting-format/1.1}relationship')
            rel_el.attrib['subject'] = report_id
            rel_el.attrib['type'] = 'isAbout'
            rel_el.attrib['ref'] = asset_id

            # TODO createdFor relationship

        from StringIO import StringIO
        sio = StringIO()
        arc.write(sio, encoding='UTF-8', xml_declaration=True)
        sio.write("\n")
        return sio.getvalue()
