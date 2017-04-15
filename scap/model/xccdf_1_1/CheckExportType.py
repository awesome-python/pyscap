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
class CheckExportType(Model):
    MODEL_MAP = {
        'attributes': {
            'value-id': {'type': 'NCName', 'required': True},
            'export-name': {'type': 'String', 'required': True},
        },
    }

    def map(self, benchmark):
        from scap.model.xccdf_1_1.BenchmarkType import BenchmarkType
        from scap.model.xccdf_1_1.GroupType import GroupType
        # go through parents till we find value referenced by
        # check_export.value_id
        parent = self.parent
        v = None
        while(not isinstance(parent, Model)):
            if isinstance(parent, BenchmarkType) \
            or isinstance(parent, GroupType):
                if parent.has_value(self.value_id):
                    v = parent.values[self.value_id]
                    break
            parent = parent.parent

        if v is None:
            raise ValueError('Could not find Value ' + self.value_id)

        # get the resolved value
        value = v.value

        return {self.export_name: value}
