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

import logging

from scap.collector.Checker import Checker
from scap.model.xccdf_1_2 import CheckOperatorEnumeration

logger = logging.getLogger(__name__)
class CheckContentRefType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(CheckContentRefType, self).__init__(host, content, parent, args)

        self.checkers = []

        self.ref_content = self.resolve_reference(content.href)
        #TODO: check that content.system & ref_content.xml_namespace match?
        if args['system'] == 'http://oval.mitre.org/XMLSchema/oval-definitions-5':
            if not hasattr(content, 'name'):
                for defn in self.ref_content.definitions.definitions:
                    logger.debug('Adding oval def ' + defn.id + ' checker')
                    self.checkers.append(Checker.load(host, defn, self, args))
            else:
                if content.name not in self.ref_content.definitions.definitions:
                    raise ValueError('Reference name ' + content.name + ' not found in oval definitions in ' + content.href)
                defn = self.ref_content.definitions.definitions[content.name]
                logger.debug('Adding oval def ' + defn.id + ' checker')
                self.checkers.append(Checker.load(host, defn, self, args))
        elif args['system'] in ['http://scap.nist.gov/schema/ocil/2', 'http://scap.nist.gov/schema/ocil/2.0']:
            if not hasattr(content, 'name'):
                for q in self.ref_content.questionnaires.questionnaires:
                    logger.debug('Adding ocil quesitonnaire ' + q.id + ' checker')
                    self.checkers.append(Checker.load(host, q, self, args))
            else:
                if content.name not in self.ref_content.questionnaires.questionnaires:
                    raise ValueError('Reference name ' + content.name + ' not found in ocil questionnaires in ' + content.href)
                q = self.ref_content.questionnaires.questionnaires[content.name]
                logger.debug('Adding ocil quesitonnaire ' + q.id + ' checker')
                self.checkers.append(Checker.load(host, q, self, args))
        else:
            logger.debug('Check system not implemented ' + args['system'])

    def _package_result(self, checker):
        check_result = {
            'result': 'notchecked',
            'messages': [],
            'instances': [],
        }

        checker_result = checker.check()

        if checker.__module__.startswith('scap.collector.checker.oval'):
            check_result['result'] = CheckOperatorEnumeration.oval_translate(checker_result['result'])
            #TODO messages, instances
            check_result['messages'] = []
            check_result['instances'] = []
        elif checker.__module__.startswith('scap.collector.checker.ocil'):
            check_result['result'] = CheckOperatorEnumeration.oval_translate(checker_result['result'])
            #TODO messages, instances
            check_result['messages'] = []
            check_result['instances'] = []

        return check_result

    def collect(self):
        if len(self.checkers) == 0:
            return [{
                'result': 'notchecked',
                'messages': [],
                'instances': [],
            }]
        elif len(self.checkers) > 1:
            # TODO: multi-check

            result = []
            for checker in self.checkers:
                result.append(self._package_result(checker))
        else:
            result = self._package_result(self.checkers[0])

        result = CheckOperatorEnumeration.AND(check_results)

        if self.content.negate:
            return CheckOperatorEnumeration.negate(result)
        else:
            return result

    def resolve_reference(self, ref):
        if ref.startswith('oval:'):
            ref_type = ref.split(':')[2]
            if ref_type == 'def' and ref in self.ref_content.definitions.definitions:
                logger.debug('Found OVAL definition ' + ref)
                return self.ref_content.definitions.definitions[ref]
            elif ref_type == 'obj' and ref in self.ref_content.objects.objects:
                logger.debug('Found OVAL object ' + ref)
                return self.ref_content.objects.objects[ref]
            elif ref_type == 'ste' and ref in self.ref_content.states.states:
                logger.debug('Found OVAL state ' + ref)
                return self.ref_content.states.states[ref]
            elif ref_type == 'tst' and ref in self.ref_content.tests.tests:
                logger.debug('Found OVAL test ' + ref)
                return self.ref_content.tests.tests[ref]
            elif ref_type == 'var' and ref in self.ref_content.variables.variables:
                logger.debug('Found OVAL variable ' + ref)
                return self.ref_content.variables.variables[ref]
            else:
                logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
                return self.parent.resolve_reference('#' + ref)
        else:
            return self.parent.resolve_reference(ref)
