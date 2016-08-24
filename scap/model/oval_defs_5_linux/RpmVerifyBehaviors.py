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
class RpmVerifyBehaviors(Model):
    MODEL_MAP = {
        'attributes': {
            'nodeps': {'type': 'Boolean', 'default': False},
            'nodigest': {'type': 'Boolean', 'default': False},
            'nofiles': {'type': 'Boolean', 'default': False},
            'noscripts': {'type': 'Boolean', 'default': False},
            'nosignature': {'type': 'Boolean', 'default': False},
            'nolinkto': {'type': 'Boolean', 'default': False},
            'nomd5': {'type': 'Boolean', 'default': False},
            'nosize': {'type': 'Boolean', 'default': False},
            'nouser': {'type': 'Boolean', 'default': False},
            'nogroup': {'type': 'Boolean', 'default': False},
            'nomtime': {'type': 'Boolean', 'default': False},
            'nomode': {'type': 'Boolean', 'default': False},
            'nordev': {'type': 'Boolean', 'default': False},
            'noconfigfiles': {'type': 'Boolean', 'default': False},
            'noghostfiles': {'type': 'Boolean', 'default': False},
        }
    }
