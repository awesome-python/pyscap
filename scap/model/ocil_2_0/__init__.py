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

TAG_MAP = {
    'artifact_ref': 'ArtifactRefType',
    'ocil': 'OCILType',
    'document': 'DocumentType',
    'boolean_question_test_action': 'BooleanQuestionTestActionType',
    'choice_question_test_action': 'ChoiceQuestionTestActionType',
    'numeric_question_test_action': 'NumericQuestionTestActionType',
    'string_question_test_action': 'StringQuestionTestActionType',
    'boolean_question': 'BooleanQuestionType',
    'choice_question': 'ChoiceQuestionType',
    'numeric_question': 'NumericQuestionType',
    'string_question': 'StringQuestionType',
    'constant_variable': 'ConstantVariableType',
    'local_variable': 'LocalVariableType',
    'external_variable': 'ExternalVariableType',
    'user': 'UserType',
    'system': 'SystemTargetType',
    'boolean_question_result': 'BooleanQuestionResultType',
    'choice_question_result': 'ChoiceQuestionResultType',
    'numeric_question_result': 'NumericQuestionResultType',
    'string_question_result': 'StringQuestionResultType',
    'questionnaire': 'QuestionnaireType',
    'when_unknown': 'TestActionConditionType',
    'when_not_tested': 'TestActionConditionType',
    'when_not_applicable': 'TestActionConditionType',
    'when_error': 'TestActionConditionType',
    'when_true': 'TestActionConditionType',
    'when_false': 'TestActionConditionType',
    'ChoiceQuestionTestActionType\when_choice': 'ChoiceTestActionConditionType',
    'when_equals': 'EqualsTestActionConditionType',
    'NumericQuestionTestActionType\when_range': 'RangeTestActionConditionType',
    'StringQuestionTestActionType\when_pattern': 'PatternTestActionConditionType',
    'when_equals': 'EqualsTestActionConditionType',
    'range': 'RangeType',
    'pattern': 'PatternType',
    'min': 'RangeValueType',
    'max': 'RangeValueType',
    'result': 'ResultType',
    'test_action_ref': 'TestActionRefType',
    'artifact_refs': 'ArtifactRefsType',
    'choice_group': 'ChoiceGroupType',
    'sub': 'SubstitutionTextType',
    'question_text': 'QuestionTextType',
    'instructions': 'InstructionsType',
    'choice': 'ChoiceType',
    'step': 'StepType',
    'questionnaire_result': 'QuestionnaireResultType',
    'test_action_result': 'TestActionResultType',
    'result': 'ResultType',
    'artifact': 'ArtifactType',
    'artifact_ref': 'ArtifactRefType',
    'artifact_result': 'ArtifactResultType',
    ### TODO
    'text_artifact_value': 'TextArtifactValueType',
    'binary_artifact_value': 'BinaryArtifactValueType',
    'reference_artifact_value': 'ReferenceArtifactValueType',
    ### /TODO
    'submitter': 'UserType',
    'when_pattern': 'SetExpressionPatternType',
    'when_choice': 'SetExpressionChoiceType',
    'when_range': 'SetExpressionRangeType',
    'when_boolean': 'SetExpressionBooleanType',
    'actions': 'OperationType',
    'test_action_ref': 'TestActionRefType',
}
