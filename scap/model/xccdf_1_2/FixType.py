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
from scap.model.xccdf_1_2.FixStrategyEnumeration import FIX_STRATEGY_ENUMERATION
from scap.model.xccdf_1_2.RatingEnumeration import RATING_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class FixType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'type': 'NCNAME'},
            'reboot': {'ignore': True, 'type': 'Boolean'},
            'strategy': {'ignore': True, 'enum': FIX_STRATEGY_ENUMERATION, 'default': 'unknown'},
            'disruption': {'ignore': True, 'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'complexity': {'ignore': True, 'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'system': {'ignore': True, 'type': 'AnyURI'},
            'platform': {'ignore': True, 'type': 'AnyURI'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.2}sub': {'append': 'subs', 'ignore': True, 'min': 0, 'max': None, 'class': 'SubType'},
            '{http://checklists.nist.gov/xccdf/1.2}instance': {'append': 'instance', 'ignore': True, 'min': 0, 'max': None, 'class': 'InstanceFixType'},
        },
    }
