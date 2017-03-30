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

from scap.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class ComponentRefElement(Checker):
    def __init__(self, host, content, parent, args=None):
        super(ComponentRefElement, self).__init__(host, content, parent, args)

        comp = self.parent.resolve_reference(content.href).model

        self.reference_mapping = content.catalog.to_dict()
        self.checker = Checker.load(host, comp, self, args)

    def collect(self):
        return self.checker.collect()

    def resolve_reference(self, ref):
        if ref in self.reference_mapping:
            return self.parent.resolve_reference(self.reference_mapping[ref])
        else:
            return self.parent.resolve_reference(ref)
