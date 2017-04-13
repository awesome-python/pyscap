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
class SelChoicesType(Model):
    MODEL_MAP = {
        'attributes': {
            'mustMatch': {'type': 'Boolean'},
            'selector': {'type': 'String', 'default': None},
        },
        'elements': {
            # TODO at least one choice/complex-choice
            '{http://checklists.nist.gov/xccdf/1.1}choice': {'class': 'scap.model.xs.String', 'append': 'choices', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}complex-choice': {'class': 'ComplexValueType', 'min': 0, 'max': 1},
        },
    }
