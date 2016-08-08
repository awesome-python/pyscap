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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class QuestionnaireResultType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}artifact_result': {'class': 'ArtifactResultType'},
        }
    }
    def __init__(self):
        super(QuestionnaireResultType, self).__init__()

        self.questionnaire_ref = None
        self.result = None

        self.artifact_results = []

    def parse_attribute(self, name, value):
        if name == 'questionnaire_ref':
            self.questionnaire_ref = value
        elif name == 'result':
            self.result = value
        else:
            return super(QuestionnaireResultType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}artifact_results':
            for sub_sub_el in sub_el:
                self.artifact_results[sub_sub_el.attrib['id']] = Model.load(self, sub_sub_el)
        else:
            return super(QuestionnaireResultType, self).parse_element(sub_el)
        return True
