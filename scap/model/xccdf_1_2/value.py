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

logger = logging.getLogger(__name__)
class Value(Content):
    def __init__(self, parent, root_el, el):
        self.parent = parent
        self.id = el.attrib['id']
        self.type = el.attrib['type']
        self.operator = el.attrib['operator']

        self.selectors = {}
        self.default = None
        for vs in el.findall('xccdf_1_2:value', Engine.namespaces):
            if 'selector' in vs.attrib:
                logger.debug('Selector value of ' + el.attrib['id'] + ' ' + vs.attrib['selector'] + ' = ' + str(vs.text))
                self.selectors[vs.attrib['selector']] = vs.text
            else:
                logger.debug('Default value of ' + el.attrib['id'] + ' is ' + str(vs.text))
                self.default = vs.text
