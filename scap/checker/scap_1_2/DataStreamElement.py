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
class DataStreamElement(Checker):
    def __init__(self, host, content, parent, args=None):
        super(DataStreamElement, self).__init__(host, content, parent, args)

        self.selected_checklist = None

        if 'checklist' in args:
            checklist_id = args[checklist]
            if checklist_id not in content.checklists:
                logger.critical('Specified --checklist, ' + checklist_id + ', not found in content. Available checklists: ' + str(list(content.checklists.keys())))
                import sys
                sys.exit()
            else:
                checklist = content.checklists[checklist_id].resolve()
        else:
            if len(content.checklists) == 1:
                checklist = list(content.checklists.values())[0].resolve()
            else:
                logger.critical('No --checklist specified and unable to implicitly choose one. Available checklists: ' + str(list(content.checklists.keys())))
                import sys
                sys.exit()
        logger.info('Selecting checklist ' + checklist.id)

        self.checklist_checker = Checker.load(host, checklist, self, args)

    def check(self):
        return self.checklist_checker.check()

    # def resolve_reference(self, ref):
    #     if ref in self.ref_mapping:
    #         logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
    #         ref = self.ref_mapping[ref]
    #
    #     if ref[0] == '#':
    #         ref = ref[1:]
    #         if ref in self.dictionaries:
    #             logger.debug('Resolving ' + ref + ' as component reference to ' + self.dictionaries[ref].href)
    #             return self.dictionaries[ref].resolve()
    #         elif ref in self.checklists:
    #             logger.debug('Resolving ' + ref + ' as component reference to ' + self.checklists[ref].href)
    #             return self.checklists[ref].resolve()
    #         elif ref in self.checks:
    #             logger.debug('Resolving ' + ref + ' as component reference to ' + self.checks[ref].href)
    #             return self.checks[ref].resolve()
    #         else:
    #             logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
    #             return self.parent.resolve_reference('#' + ref)
    #     else:
    #         logger.critical('only local references are supported: ' + ref)
    #         import sys
    #         sys.exit()
