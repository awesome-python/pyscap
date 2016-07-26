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

from scap.collector.ResultCollector import ResultCollector
import logging
from scap.model.xccdf_1_2.Rule import Rule

logger = logging.getLogger(__name__)
class RuleCollector(ResultCollector):
    def __init__(self, host, content, values, check_selector):
        super(RuleCollector, self).__init__(host, content)

        self.values = values
        self.check_selector = check_selector

    def collect_results(self):
        if self.check_selector not in self.content.checks:
            logger.critical('Check selector ' + self.check_selector + ' not found for rule ' + self.content.id)
            import sys
            sys.exit()
        check = self.content.checks[self.check_selector]

        from scap.model.xccdf_1_2.Check import Check
        from scap.model.xccdf_1_2.ComplexCheck import ComplexCheck
        if isinstance(check, Check):
            from scap.collector.result.xccdf_1_2.CheckCollector import CheckCollector
            col = CheckCollector(self.host, check, self.values)
            self.host.results[self.content.id] = col.collect_results()
        elif isinstance(check, ComplexCheck):
            from scap.collector.result.xccdf_1_2.ComplexCheckCollector import ComplexCheckCollector
            col = ComplexCheckCollector(self.host, check, self.values)
            self.host.results[self.content.id] = col.collect_results()
        else:
            logger.warning('Unknown check type ' + check.__class__.__name__ + ' for rule ' + self.content.id)
            self.host.results[self.content.id] = Rule.Result.ERROR

        logger.debug('Result of rule ' + self.content.id + ': ' + self.host.results[self.content.id])
