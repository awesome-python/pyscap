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
from scap.model.xccdf_1_2.benchmark import Benchmark

logger = logging.getLogger(__name__)
class DataStream(Content):
    def __init__(self, parent, root_el, el):
        self.parent = parent

        self.checklists = {}
        xpath = "./scap_1_2:checklists"
        xpath += "/scap_1_2:component-ref"
        for c in el.findall(xpath, Engine.namespaces):
            checklist_id = c.attrib['{' + Engine.namespaces['xlink'] + '}href'][1:]
            self.checklists[checklist_id] = Benchmark(self, root_el, root_el.find("./scap_1_2:component[@id='" + checklist_id + "']", Engine.namespaces))

    def select_rules(self, args):
        if args.checklist:
            checklist_id = args.checklist[0]
            if checklist_id not in self.checklists:
                logger.critical('Specified --checklist, ' + checklist_id + ', not found in content. Available checklists: ' + str(self.checklists.keys()))
                sys.exit()
            else:
                return self.checklists[checklist_id].select_rules(args)
        else:
            if len(self.checklists) == 1:
                return self.checklists.values()[0].select_rules(args)
            else:
                logger.critical('No --checklist specified and unable to implicitly choose one. Available checklists: ' + str(self.checklists.keys()))
                sys.exit()
