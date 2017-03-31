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
from scap.model.xccdf_1_1 import CheckOperatorEnumeration

logger = logging.getLogger(__name__)
class CheckType(Checker):
    def __init__(self, host, content, parent, args=None):
        super(CheckType, self).__init__(host, content, parent, args)

        args = {
            'system': content.system,
        }
        self.checker = None

        if len(content.check_content_refs) <= 0:
            #TODO: load check-content
            raise NotImplementedError('check-content is not supported yet')
        else:
            for ref in content.check_content_refs:
                try:
                    self.checker = Checker.load(host, ref, self, args)
                except Exception as e:
                    logger.warning('Could not load checker for ' + str(ref) + ': ' + str(e))
                    pass
                else:
                    # we got a checker, so break out of the for loop
                    break

    def collect(self):
        if self.checker is None:
            logger.debug('Never found a checker')
            return [{
                'result': 'notchecked',
                'messages': [],
                'instances': [],
            }]

        results = self.checker.collect()

        if self.content.multi_check:
            pass
        else:
            result = CheckOperatorEnumeration.AND([cr['result'] for cr in results])
            logger.debug('Combined results into ' + result + ' result')
            messages = [cr['messages'] for cr in results]
            instances = [cr['instances'] for cr in results]
            # TODO: if the rule failed and we got a fix, apply the fix & check again before appending
            results = [{
                'result': result,
                'messages': messages,
                'instances': instances,
            }]

        if self.content.negate:
            negated = []
            for r in results:
                negated.append({
                    'result': CheckOperatorEnumeration.negate(r['result']),
                    'messages': r['messages'],
                    'instances': r['instances'],
                })
            logger.debug('Negated final results: ' + str(negated))
            return negated
        else:
            logger.debug('Check final results: ' + str(negated))
            return results
