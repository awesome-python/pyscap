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

from scap.model.content import Content
import logging
from scap.engine.engine import Engine
from scap.model.xccdf_1_2.profile import Profile

logger = logging.getLogger(__name__)
class Benchmark(Content):
    def __init__(self, root_el, el):
        self.profiles = {}

        xpath = "./xccdf_1_2:Benchmark"
        xpath += "/xccdf_1_2:Profile"
        for p in self.checklist.findall(xpath, Engine.namespaces):
            profiles[p.attrib['id']] = Profile(p)
        # if 'profile' in args:
        #     if args['profile'] not in profiles:
        #         logger.critical('Specified --profile, ' + args['profile'] + ', not found in content. Available profiles: ' + str(profiles.keys()))
        #         sys.exit()
        #     else:
        #         self.profile = profiles[args['data_stream']]
        # else:
        #     if len(profiles) == 1:
        #         self.profile = profiles.values()[0]
        #     else:
        #         logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(profiles.keys()))
        #         sys.exit()
        # if 'extends' in self.profile.attrib:
        #     logger.critical('Profiles with @extends are not supported')
        #     sys.exit()
        # logger.info('Using profile ' + self.profile.attrib['id'])
        #
        # self.rules = {}
        # xpath = ".//xccdf_1_2:Rule"
        # for r in self.checklist.findall(xpath, Engine.namespaces):
        #     xpath = "./xccdf_1_2:select[@idref='" + r.attrib['id'] + "']"
        #     s = self.profile.find(xpath, Engine.namespaces)
        #     if s is not None:
        #         if s.attrib['selected'] == 'true':
        #             logger.info('Rule selected by profile: ' + r.attrib['id'])
        #             self.rules[r.attrib['id']] = r
        #     else:
        #         if r.attrib['selected'] == 'true':
        #             logger.info('Rule selected by default: ' + r.attrib['id'])
        #             self.rules[r.attrib['id']] = r
        #
        # self.values = {}
        # xpath = ".//xccdf_1_2:Value"
        # for v in self.checklist.findall(xpath, Engine.namespaces):
        #     v_id = v.attrib['id']
        #     logger.debug('Collecting value ' + v_id)
        #     self.values[v_id] = { 'element': v }
        #     selectors = {}
        #     for vs in v.findall('xccdf_1_2:value', Engine.namespaces):
        #         if 'selector' in vs.attrib:
        #             logger.debug('Selector value of ' + v_id + ' ' + vs.attrib['selector'] + ' = ' + str(vs.text))
        #             selectors[vs.attrib['selector']] = vs.text
        #         else:
        #             logger.debug('Default value of ' + v_id + ' is ' + str(vs.text))
        #             self.values[v_id]['value'] = vs.text
        #     xpath = "./xccdf_1_2:refine-value[@idref='" + v_id + "']"
        #     rv = self.profile.find(xpath, Engine.namespaces)
        #     if rv is not None:
        #         logger.info('Modifying value ' + v_id + ' by profile ' + self.profile.attrib['id'] + ' using selector ' + rv.attrib['selector'])
        #         self.values[v_id]['value'] = selectors[rv.attrib['selector']]
        #     logger.info('Using ' + v.attrib['type'] + ' ' + v.attrib['operator'] + ' ' + str(self.values[v_id]['value']) + ' for value ' + v_id)

    def select_rules(self):
        # b_args = {}
        # if args.data_stream:
        #     b_args['data_stream'] = args.data_stream[0]
        #     if args.checklist:
        #         b_args['checklist'] = args.checklist[0]
        # if args.profile:
        #     b_args['profile'] = args.profile[0]

        # if 'checklist' in args:
        #     if args['checklist'] not in checklist_ids:
        #         logger.critical('Specified --checklist, ' + args['checklist'] + ', not found in content. Available checklists: ' + str(checklist_ids))
        #         sys.exit()
        #     else:
        #         checklist_id = args['checklist']
        # else:
        #     if len(checklist_ids) == 1:
        #         checklist_id = checklist_ids[0]
        #     else:
        #         logger.critical('No --checklist specified and unable to implicitly choose one. Available checklists: ' + str(checklist_ids))
        #         sys.exit()

        pass
