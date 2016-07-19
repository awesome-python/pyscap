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
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Profile(Model):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        self.id = el.attrib['id']

        if 'extends' in el.attrib:
            logger.critical('Profiles with @extends are not supported')
            sys.exit()

        self.rules = {}
        for r in parent.rules.values():
            xpath = "./xccdf_1_2:select[@idref='" + r.id + "']"
            s = el.find(xpath, Engine.namespaces)
            if s is not None:
                if s.attrib['selected'] == 'true':
                    logger.info('Rule selected by profile: ' + r.id)
                    self.rules[r.id] = r
            else:
                if r.selected:
                    logger.info('Rule selected by default: ' + r.id)
                    self.rules[r.id] = r

            xpath = "./xccdf_1_2:refine-rule[@idref='" + r.id + "']"
            s = el.find(xpath, Engine.namespaces)
            if s is not None:
                logger.info('Selecting check ' + s.attrib['selector'] + ' for rule ' + r.id)
                r.select_check(s.attrib['selector'])

        self.values = {}
        for v in parent.values.values():
            logger.debug('Collecting value ' + v.id)
            self.values[v.id] = { 'model': v }
            self.values[v.id]['value'] = v.default

            xpath = "./xccdf_1_2:refine-value[@idref='" + v.id + "']"
            rv = el.find(xpath, Engine.namespaces)
            if rv is not None:
                logger.info('Modifying value ' + v.id + ' by profile ' + el.attrib['id'] + ' using selector ' + rv.attrib['selector'])
                self.values[v.id]['value'] = v.selectors[rv.attrib['selector']]

            logger.info('Using ' + v.type + ' ' + v.operator + ' ' + str(self.values[v.id]['value']) + ' for value ' + v.id)
