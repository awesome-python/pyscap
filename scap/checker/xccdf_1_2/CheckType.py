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
class CheckType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(CheckType, self).__init__(host, content, parent, args)

        self.checkers = []
        content = self.resolve()
        if isinstance(content, list):
            for defn in content:
                self.checkers.append(Checker.load(host, defn, self, args))
        else:
            self.checkers.append(Checker.load(host, content, self, args))

    def check(self):
        # TODO: multi-check

        from scap.model.xccdf_1_2 import CheckOperatorEnumeration
        results = []
        for checker in self.checkers:
            if checker.content.model_namespace.startswith('oval'):
                results.append(CheckOperatorEnumeration.oval_translate(checker.check()))
            elif checker.content.model_namespace.startswith('ocil'):
                results.append(CheckOperatorEnumeration.ocil_translate(checker.check()))
            else:
                raise NotImplementedError('Unknown model namespace: ' + checker.content.model_namespace)

        result = CheckOperatorEnumeration.AND(results)

        if self.content.negate:
            return CheckOperatorEnumeration.negate(result)
        else:
            return result

    # def resolve(self):
    #     content = self.resolve_reference(self.check_content_ref)
    #     if self.system == 'http://oval.mitre.org/XMLSchema/oval-definitions-5':
    #         if self.check_content_name is None:
    #             return list(content.definitions.values())
    #         else:
    #             # looking for a definition
    #             return content.definitions[self.check_content_name]
    #     elif self.system == 'http://scap.nist.gov/schema/ocil/2' or self.system == 'http://scap.nist.gov/schema/ocil/2.0':
    #         if self.check_content_name is None:
    #             return content
    #         else:
    #             logger.debug('Looking in ocil content "' + content.document.title + '" for ' + self.check_content_name)
    #             id_parts = self.check_content_name.split(':')
    #             if id_parts[2] == 'questionnaire':
    #                 # looking for a questionnaire
    #                 return content.questionnaires[self.check_content_name]
    #             else:
    #                 raise NotImplementedError('Checking of OCIL ' + id_parts[2] + ' content is not implemented')
    #     else:
    #         print(str(content))
    #         raise NotImplementedError('Check system not implemented ' + self.system)
