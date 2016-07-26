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
class ComponentGroup(Model):
    def __init__(self):
        super(ComponentGroup, self).__init__()

        self.components = []

    def parse_sub_el(self, sub_el):
        sub_el_tags = {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}object_component': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variable_component': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}literal_component': True,

            # collapse FunctionGroup into ComponentGroup
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}arithmetic': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}begin': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}concat': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}count': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}end': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}escape_regex': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}split': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}substring': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}time_difference': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}unique': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}regex_capture': True,
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}glob_to_regex': True,
        }

        if sub_el.tag in sub_el_tags:
            self.components.append(Model.load_child(self, sub_el))
        else:
            return super(ComponentGroup, self).parse_sub_el(sub_el)
        return True
