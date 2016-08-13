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
class OVALDefintionsType(Model):
    MODEL_MAP = {
        'xml_schema': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
        'tag_name' : 'oval_definitions',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-common-5}generator': {'class': 'GeneratorType'},

            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}definitions': {'class': 'DefinitionsType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}tests': {'class': 'TestsType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}objects': {'class': 'ObjectsType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}states': {'class': 'StatesType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variables': {'class': 'VariablesType'},
            '{http://www.w3.org/2000/09/xmldsig#}Signature': {'ignore': True},
        }
    }

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            ref = self.ref_mapping[ref]

        if ref.startswith('oval:'):
            ref_type = ref.split(':')[2]
            if ref_type == 'def' and ref in self.definitions:
                #logger.debug('Found OVAL definition ' + ref)
                return self.definitions[ref]
            elif ref_type == 'obj' and ref in self.objects:
                #logger.debug('Found OVAL object ' + ref)
                return self.objects[ref]
            elif ref_type == 'ste' and ref in self.states:
                #logger.debug('Found OVAL state ' + ref)
                return self.states[ref]
            elif ref_type == 'tst' and ref in self.tests:
                #logger.debug('Found OVAL test ' + ref)
                return self.tests[ref]
            elif ref_type == 'var' and ref in self.variables:
                #logger.debug('Found OVAL variable ' + ref)
                return self.variables[ref]
            else:
                #logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
                return self.parent.resolve_reference('#' + ref)
        else:
            return self.parent.resolve_reference(ref)
