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
class ResultsType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}title': {'class': 'TextType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}questionnaire_results': {'class': 'QuestionnaireResultsType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}test_action_results': {'class': 'TestActionResultsType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}question_results': {'class': 'QuestionResultsType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}artifact_results': {'class': 'ArtifactResultsType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}targets': {'class': 'TargetsType', 'min': 0, 'max': 1},
        },
        'attributes': {
            'start_time': {'type': 'DateTime'},
            'end_time': {'type': 'DateTime'},
        }
    }
