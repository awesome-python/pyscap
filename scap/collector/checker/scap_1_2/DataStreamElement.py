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

from scap.collector.Checker import Checker
import logging

logger = logging.getLogger(__name__)
class DataStreamElement(Checker):
    def __init__(self, host, content, parent, args=None):
        super(DataStreamElement, self).__init__(host, content, parent, args)

        if 'checklist' in args:
            checklist_id = args[checklist]
            if checklist_id not in content.checklists:
                logger.critical('Specified --checklist, ' + checklist_id + ', not found in content. Available checklists: ' + str(list(content.checklists.keys())))
                import sys
                sys.exit()
            else:
                comp_ref = content.checklists[checklist_id]
        else:
            if len(content.checklists) == 1:
                comp_ref = list(content.checklists.values())[0]
            else:
                logger.critical('No --checklist specified and unable to implicitly choose one. Available checklists: ' + str(list(content.checklists.keys())))
                import sys
                sys.exit()
            checklist_id = comp_ref.id
        logger.info('Selecting checklist ' + checklist_id)
        self.host.facts['selected_checklist'] = checklist.id

        self.checker = Checker.load(host, comp_ref, self, args)

    def collect(self):
        return self.checker.collect()

    def resolve_reference(self, ref):
        if ref[0] == '#':
            ref = ref[1:]
            if ref in self.content.dictionaries:
                logger.debug('Resolving ' + ref + ' as component reference to ' + self.content.dictionaries[ref].href)
                return self.parent.resolve_reference(self.content.dictionaries[ref].href).model
            elif ref in self.content.checklists:
                logger.debug('Resolving ' + ref + ' as component reference to ' + self.content.checklists[ref].href)
                return self.parent.resolve_reference(self.content.checklists[ref].href).model
            elif ref in self.content.checks:
                logger.debug('Resolving ' + ref + ' as component reference to ' + self.content.checks[ref].href)
                return self.parent.resolve_reference(self.content.checks[ref].href).model
            else:
                logger.debug('Reference ' + ref + ' not in ' + self.content.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
                return self.parent.resolve_reference('#' + ref)
        else:
            logger.critical('only local references are supported: ' + ref)
            import sys
            sys.exit()
