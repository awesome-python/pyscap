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
from scap.Engine import Engine
import logging

logger = logging.getLogger(__name__)
class RuleCollector(ResultCollector):
    def __init__(self, host, content, values, check_selector):
        super(RuleCollector, self).__init__(host, content)

        self.values = values
        self.check_selector = check_selector

    def collect_results(self):
        from scap.model.xccdf_1_2.Check import Check
        self.host.results[self.content.id] = Check.Result.NOT_CHECKED
        logger.debug('Result of rule ' + self.content.id + ': ' + self.host.results[self.content.id])
