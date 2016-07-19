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

from scap.model.Simple import Simple
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Benchmark(Simple):
    def __init__(self):
        super(Benchmark, self).__init__()

        self.rules = {}
        self.values = {}
        self.profiles = {}

    def parse_attrib(self, name, value):
        if name == 'Id':
            pass
        elif name == 'resolved':
            pass
        elif name == 'style':
            pass
        elif name == 'style-href':
            pass
        else:
            return super(Benchmark, self).parse_attrib(name, value)
        return True

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}status':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}dc-status':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}title':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}description':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}notice':
            logger.info('Notice: ' + sub_el.text)
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}front-matter':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}rear-matter':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}reference':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}plain-text':
            pass
        elif sub_el.tag == '{http://cpe.mitre.org/language/2.0}platform-specification':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}platform':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}version':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}metadata':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}model':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Profile':
            from scap.model.xccdf_1_2.Profile import Profile
            logger.debug('found profile ' + sub_el.attrib['id'])
            p = Profile()
            p.from_xml(self, sub_el)
            self.profiles[sub_el.attrib['id']] = p
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Value':
            from scap.model.xccdf_1_2.Value import Value
            v = Value()
            v.from_xml(self, sub_el)
            self.values[sub_el.attrib['id']] = v
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Group':
            from scap.model.xccdf_1_2.Group import Group
            g = Group()
            g.from_xml(self, sub_el)
            self.rules.update(g.get_rules())
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Rule':
            from scap.model.xccdf_1_2.Rule import Rule
            r = Rule()
            r.from_xml(self, sub_el)
            self.rules[sub_el.attrib['id']] = r
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}TestResult':
            pass
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}signature':
            pass
        else:
            return super(Benchmark, self).parse_sub_el(name, value)
        return True
