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
class Test(Checker):
    def __init__(self, host, content, args=None):
        super(Test, self).__init__(host, content, args)

        self.object = content.resolve_object()
        self.states = content.resolve_states()

    def check(self):
        # collect items matching obj
        items, existence_results = self.collect_object_items()

        # existence check
        from scap.model.oval_defs_5 import ExistenceEnumeration
        if self.content.check_existence == 'all_exist':
            existence_result = ExistenceEnumeration.all_exist(existence_results)
        elif self.content.check_existence == 'any_exist':
            existence_result = ExistenceEnumeration.any_exist(existence_results)
        elif self.content.check_existence == 'at_least_one_exists':
            existence_result = ExistenceEnumeration.at_least_one_exists(existence_results)
        elif self.content.check_existence == 'none_exist':
            existence_result = ExistenceEnumeration.none_exist(existence_results)
        elif self.content.check_existence == 'only_one_exists':
            existence_result = ExistenceEnumeration.only_one_exists(existence_results)
        else:
            raise ValueError('Test ' + self.content.id + ' check_existence value is unknown: ' + self.content.check_existence)

        # if no oval states, return true
        if len(self.states) == 0:
            return 'true'

        # for each item
        from scap.model.oval_defs_5 import OperatorsEnumeration
        item_results = []
        for item in items:
            # for each state, compare item with state
            item_state_results = []
            for state in self.states:
                item_state_results.append(self.eval_item_state(item, state))

            # combine results with state_operator
            if self.content.state_operator == 'AND':
                item_results.append(OperatorsEnumeration.AND(item_state_results))
            elif self.content.state_operator == 'ONE':
                item_results.append(OperatorsEnumeration.ONE(item_state_results))
            elif self.content.state_operator == 'OR':
                item_results.append(OperatorsEnumeration.OR(item_state_results))
            elif self.content.state_operator == 'XOR':
                item_results.append(OperatorsEnumeration.XOR(item_state_results))
            else:
                raise ValueError('Test ' + self.content.id + ' state_operator value is unknown: ' + self.content.state_operator)

        # see if check is satisfied
        from scap.model.oval_defs_5 import CheckEnumeration
        if self.content.check == 'all':
            result = CheckEnumeration.all(item_results)
        elif self.content.check == 'at least one':
            result = CheckEnumeration.at_least_one(item_results)
        elif self.content.check == 'none satisfy':
            result = CheckEnumeration.none_satisfy(item_results)
        elif self.content.check == 'only one':
            result = CheckEnumeration.only_one(item_results)
        else:
            raise ValueError('Test ' + self.content.id + ' check value is unknown: ' + self.content.check)

        return result

    def collect_object_items(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def eval_item_state(self, item, state):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
