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

SYSTEM_ENUMERATION = [
    'http://oval.mitre.org/XMLSchema/oval-definitions-5',
    'http://scap.nist.gov/schema/ocil/2.0',
    'http://scap.nist.gov/schema/ocil/2',
]
logger = logging.getLogger(__name__)
class CheckType(Model):
    MODEL_MAP = {
        'attributes': {
            'system': {'type': 'AnyURI', 'required': True},
            'negate': {'type': 'Boolean', 'default': False},
            'id': {'type': 'NCName'},
            'selector': {'default': None, 'type': 'String'},
            'multi-check': {'type': 'Boolean', 'default': False},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}check-import': {'class': 'CheckImportType', 'append': 'check_imports', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}check-export': {'class': 'CheckExportType', 'append': 'check_exports', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}check-content-ref': {'class': 'CheckContentRefType', 'append': 'check_content_refs', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}check-content': {'class': 'CheckContentType', 'min': 0, 'max': 1},
        },
    }

    def __str__(self):
        if self.system == 'http://oval.mitre.org/XMLSchema/oval-definitions-5':
            s = 'oval-definitions-5:'
        elif self.system == 'http://scap.nist.gov/schema/ocil/2.0':
            s = 'ocil-2.0:'
        elif self.system == 'http://scap.nist.gov/schema/ocil/2':
            s = 'ocil-2:'
        else:
            return self.system

        if hasattr(self, 'id'):
            s += self.id + ':'

        if len(self.check_content_refs) > 0:
            s += str([ref.href + ('' if not hasattr(ref, 'name') else '#' + ref.name) for ref in self.check_content_refs])
        return s
