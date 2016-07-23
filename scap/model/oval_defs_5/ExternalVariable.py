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

from scap.model.oval_defs_5.variable import Variable
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class ExternalVariable(Variable):
    def __init__(self):
        super(ExternalVariable, self).__init__()

        self.tag_name = '{http://oval.mitre.org/XMLSchema/oval-definitions-5}external_variable'

    def from_xml(self, parent, el):
        super(ExternalVariable, self).from_xml(parent, el)

        self.possible_values = {}
        for pv_el in el.findall('./oval_defs_5:possible_value'):
            if 'hint' not in pv_el.attrib:
                logger.critical('possible_value element missing hint attribute')
                import sys
                sys.exit()
            if 'value' not in pv_el.attrib:
                logger.critical('possible_value element missing value attribute')
                import sys
                sys.exit()
            self.possible_values[pv_el.attrib['value']] = pv_el.attrib['hint']

        self.possible_restrictions = []
        for pr_el in el.findall('./oval_defs_5:possible_restriction'):
            if 'hint' not in pr_el.attrib:
                logger.critical('possible_restriction element missing hint attribute')
                import sys
                sys.exit()
            if 'operation' not in pr_el.attrib:
                logger.critical('possible_restriction element missing operation attribute')
                import sys
                sys.exit()
            restrictions = []
            for r_el in pr_el:
                if 'value' not in r_el.attrib:
                    logger.critical('restriction element missing value attribute')
                    import sys
                    sys.exit()
                if 'operation' not in r_el.attrib:
                    logger.critical('restriction element missing operation attribute')
                    import sys
                    sys.exit()
                restrictions.append({'value': r_el.attrib['value'], 'operation': r_el.attrib['operation']})
            pr = {
                'hint': pr_el.attrib['hint'],
                'operation': pr_el.attrib['operation'],
                'restrictions': restrictions,
            }
            self.possible_restrictions.append(pr)
