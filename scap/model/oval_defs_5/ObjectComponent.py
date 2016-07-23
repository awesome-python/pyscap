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
class ObjectComponent(Model):
    def __init__(self):
        super(LiteralComponent, self).__init__()

        self.object_ref = None
        self.item_field = None
        self.record_field = None

        self.tag_name = '{http://oval.mitre.org/XMLSchema/oval-definitions-5}literal_component'

    def parse_attribute(self, name, value):
        if name == 'object_ref':
            self.object_ref = value
        elif name == 'item_field':
            self.item_field = value
        elif name == 'record_field':
            self.record_field = value
        else:
            return super(ObjectComponent, self).parse_attribute(name, value)
        return True
