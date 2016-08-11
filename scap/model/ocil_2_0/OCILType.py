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
            '{http://scap.nist.gov/schema/ocil/2.0}generator': {'class': 'GeneratorType', 'required': True},
            '{http://scap.nist.gov/schema/ocil/2.0}document': {'class': 'DocumentType'},
            '{http://scap.nist.gov/schema/ocil/2.0}questionnaires': {
                'list': 'questionnaires',
                'required': True,
                'classes': {
                    '{http://scap.nist.gov/schema/ocil/2.0}questionnaire': 'QuestionnaireType',
                },
            },
            '{http://scap.nist.gov/schema/ocil/2.0}test_actions': {
                'list': 'test_actions',
                'required': True,
                'classes': {
                    '{http://scap.nist.gov/schema/ocil/2.0}boolean_question_test_action': {'class': 'BooleanQuestionTestActionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}choice_question_test_action': {'class': 'ChoiceQuestionTestActionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}numeric_question_test_action': {'class': 'NumericQuestionTestActionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}string_question_test_action': {'class': 'StringQuestionTestActionElement'},
                },
            },
            '{http://scap.nist.gov/schema/ocil/2.0}questions': {
                'list': 'questions',
                'required': True,
                'classes': {
                    '{http://scap.nist.gov/schema/ocil/2.0}boolean_question': {'class': 'BooleanQuestionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}choice_question': {'class': 'ChoiceQuestionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}numeric_question': {'class': 'NumericQuestionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}string_question': {'class': 'StringQuestionElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}choice_group': {'class': 'ChoiceGroupType'},
                },
            },
            '{http://scap.nist.gov/schema/ocil/2.0}artifacts': {
                'list': 'artifacts',
                'classes': {
                    '{http://scap.nist.gov/schema/ocil/2.0}artifact': {'class': 'ArtifactElement'},
                },
            },
            '{http://scap.nist.gov/schema/ocil/2.0}variables': {
                'list': 'variables',
                'classes': {
                    '{http://scap.nist.gov/schema/ocil/2.0}constant_variable': {'class': 'ConstantVariableElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}local_variable': {'class': 'LocalVariableElement'},
                    '{http://scap.nist.gov/schema/ocil/2.0}external_variable': {'class': 'ExternalVariableElement'},
                },
            },
            '{http://scap.nist.gov/schema/ocil/2.0}results': {'class': 'ResultsElement'},
        }
    }
