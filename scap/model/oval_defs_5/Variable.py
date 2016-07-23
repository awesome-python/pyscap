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

logger = logging.getLogger(__name__)
class Variable(Model):
    @staticmethod
    def load(parent, var_el):
        # from scap.model.oval_defs_5_windows.RegistryState import RegistryState
        # from scap.model.oval_defs_5_windows.WUAUpdateSearcherState import WUAUpdateSearcherState
        var_map = {
        }
        if var_el.tag not in var_map:
            logger.critical('Unknown var tag: ' + var_el.tag)
            import sys
            sys.exit()
        var = var_map[var_el.tag]()
        var.from_xml(parent, var_el)
        return var

    # abstract
    def __init__(self, tag_name=None):
        super(Variable, self).__init__(tag_name)

        self.datatype = None

        self.ignore_attributes.extend([
            'version',
            'comment',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated variable ' + self.id)
        elif name == 'datatype':
            self.datatype = value
        else:
            return super(Variable, self).parse_attribute(name, value)
        return True
