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
class ProfileCollector(ResultCollector):
    def collect_results(self):
        for rule_id, rule in self.content.rules.items():
            from scap.collector.result.xccdf_1_2.RuleCollector import RuleCollector
            self.host.add_result_collector(RuleCollector(self.host, rule, self.args, self.content.values))
