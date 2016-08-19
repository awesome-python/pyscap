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
class OCILType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}generator': {'class': 'GeneratorType', 'min': 1, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}document': {'class': 'DocumentType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}questionnaires': {'class': 'QuestionnairesType', 'min': 1, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}test_actions': {'class': 'TestActionsType', 'min': 1, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}questions': {'class': 'QuestionsType', 'min': 1, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}artifacts': {'class': 'ArtifactsType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}variables': {'class': 'VariablesType', 'min': 0, 'max': 1},
            '{http://scap.nist.gov/schema/ocil/2.0}results': {'class': 'ResultsElement', 'min': 0, 'max': 1},
        }
    }
