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

logger = logging.getLogger(__name__)
class data_stream(ResultCollector):
    def collect(self):
        if self.args.checklist:
            checklist_id = self.args.checklist[0]
            if checklist_id not in self.content.checklists:
                logger.critical('Specified --checklist, ' + checklist_id + ', not found in content. Available checklists: ' + str(self.content.checklists.keys()))
                import sys
                sys.exit()
            else:
                checklist = self.content.checklists[checklist_id].resolve()
        else:
            if len(self.content.checklists) == 1:
                checklist = self.content.checklists.values()[0].resolve()
            else:
                logger.critical('No --checklist specified and unable to implicitly choose one. Available checklists: ' + str(self.content.checklists.keys()))
                import sys
                sys.exit()
        logger.info('Selecting checklist ' + checklist.id)

        return ResultCollector.load(self.host, checklist, self.args).collect()
