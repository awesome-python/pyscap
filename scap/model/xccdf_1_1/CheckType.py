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

    SUPPORTED_SYSTEM_ENUMERATION = [
        'http://oval.mitre.org/XMLSchema/oval',
        'http://www.cisecurity.org/xccdf/interactive/1.0',
    ]

    def __str__(self):
        if self.system == 'http://oval.mitre.org/XMLSchema/oval-definitions-5':
            s = 'oval-definitions-5:'
        elif self.system == 'http://scap.nist.gov/schema/ocil/2.0':
            s = 'ocil-2.0:'
        elif self.system == 'http://scap.nist.gov/schema/ocil/2':
            s = 'ocil-2:'
        else:
            s = self.system + ':'

        if self.id is not None:
            s += self.id + ':'

        if len(self.check_content_refs) > 0:
            s += str([ref.href + ('' if not hasattr(ref, 'name') else '#' + ref.name) for ref in self.check_content_refs])
        return s

    def check(self, benchmark, host):
        if self.system not in self.SUPPORTED_SYSTEM_ENUMERATION:
            return {
                'result': 'notchecked',
                'message': 'System ' + self.system + ' is not supported',
                'imports': {}
            }

        # This element identifies a value to be retrieved from the checking
        # system during testing of a target system. The value-id attribute is
        # merely a locally unique id. It must match the id attribute of a Value
        # object in the Benchmark.
        import_names = []
        for check_import in self.check_imports:
            import_names += check_import.import_name

        # This specifies a mapping from an XCCDF Value object to a checking
        # system variable. The value-id attribute must match the id attribute of
        # a Value object in the Benchmark.
        exports = {}
        for check_export in self.check_exports:
            exports.update(check_export.map(benchmark))

        # If two or more check-content-ref elements appear, then they represent
        # alternative locations from which a tool may obtain the check content.
        # Tools should process the alternatives in order, and use the first one
        # found.
        result = {
            'result': 'notchecked',
            'message': 'No checks available',
            'imports': {}
        }
        for check_ref in self.check_content_refs:
            result = check_ref.check(host, exports, import_names)
            if result['result'] not in ['error', 'unknown', 'notchecked']:
                break
            # otherwise, we keep trying check_refs

        # If both check-content-ref elements and check-content elements appear,
        # tools should use the check-content only if all references are
        # inaccessible.
        if result['result'] not in ['error', 'unknown', 'notchecked']:
            # try check content
            result = self.check_content.check(host)

        for check_import in self.check_imports:
            if 'imports' not in result \
            or check_import.import_name not in result['imports']:
                raise ValueError('Expected import not returned by check: ' + check_import.import_name)

        return result
