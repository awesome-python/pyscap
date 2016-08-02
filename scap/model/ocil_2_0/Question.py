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

from scap.model.ocil_2_0.ItemBase import ItemBase
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class Question(ItemBase):
    def __init__(self):
        super(Question, self).__init__()

        self.question_texts = []
        self.instructions = []

        # self.ignore_attributes.extend([
        # ])
        # self.ignore_sub_elements.extend([
        # ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}instructions':
            self.instructions.append(Model.load_child(self, sub_el))
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}question_text':
            self.question_texts.append(Model.load_child(self, sub_el))
        else:
            return super(Question, self).parse_sub_el(sub_el)
        return True
