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
from scap.model.xccdf_1_2.rule import Rule
from scap.model.xccdf_1_2.value import Value

logger = logging.getLogger(__name__)
class Benchmark(Content):
    def __init__(self, parent, root_el, el):
        self.parent = parent

        self.rules = {}
        xpath = ".//xccdf_1_2:Rule"
        for r in el.findall(xpath, Engine.namespaces):
            self.rules[r.attrib['id']] = Rule(self, root_el, r)

        self.values = {}
        xpath = ".//xccdf_1_2:Value"
        for v in el.findall(xpath, Engine.namespaces):
            self.values[v.attrib['id']] = Value(self, root_el, v)

        # load profiles last so they can find .rules and .values
        self.profiles = {}
        xpath = "./xccdf_1_2:Benchmark"
        xpath += "/xccdf_1_2:Profile"
        for p in el.findall(xpath, Engine.namespaces):
            self.profiles[p.attrib['id']] = Profile(self, root_el, p)

    def select_rules(self, args):
        if args.profile:
            profile_id = args.profile[0]
            if profile_id not in self.profiles:
                logger.critical('Specified --profile, ' + profile_id + ', not found in content. Available profiles: ' + str(self.profiles.keys()))
                sys.exit()
            else:
                return self.profiles[profile_id].select_rules()
        else:
            if len(self.profiles) == 1:
                return self.profiles.values()[0].select_rules()
            else:
                logger.critical('No --profile specified and unable to implicitly choose one. Available profiles: ' + str(self.profiles.keys()))
                sys.exit()
