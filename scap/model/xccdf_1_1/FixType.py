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
from scap.model.xccdf_1_1.FixStrategyEnumeration import FIX_STRATEGY_ENUMERATION
from scap.model.xccdf_1_1.RatingEnumeration import RATING_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class FixType(Model):
    MODEL_MAP = {
        'attributes': {
            'id': {'type': 'NCName'},
            'reboot': {'type': 'Boolean'},
            'strategy': {'enum': FIX_STRATEGY_ENUMERATION, 'default': 'unknown'},
            'disruption': {'ignore': True, 'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'complexity': {'ignore': True, 'enum': RATING_ENUMERATION, 'default': 'unknown'},
            'system': {'type': 'AnyURI'},
            'platform': {'type': 'AnyURI'},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}sub': {'append': 'subs', 'ignore': True, 'min': 0, 'max': None, 'class': 'SubType'},
            '{http://checklists.nist.gov/xccdf/1.1}instance': {'append': 'instance', 'ignore': True, 'min': 0, 'max': None, 'class': 'InstanceFixType'},
        },
    }

    SYSTEM_ENUMERATION = [
        # 'urn:xccdf:fix:commands',
        # # This specifies that the content of the fix element is a list of target
        # # system commands; executed in order, the commands should bring the
        # # target system into compliance with the Rule.
        #
        # 'urn:xccdf:fix:urls',
        # # This specifies that the content of the fix element is a list of one or
        # # more URLs. The resources identified by the URLs should be applied to
        # # bring the system into compliance with the Rule.
        #
        # 'urn:xccdf:fix:script:sh', # Bourne shell
        # 'urn:xccdf:fix:script:csh', # C Shell
        # 'urn:xccdf:fix:script:perl', # Perl
        # 'urn:xccdf:fix:script:batch', # Windows batch script
        # 'urn:xccdf:fix:script:python', # Python and all Python-based scripting languages
        # 'urn:xccdf:fix:script:vbscript', # Visual Basic Script (VBS)
        # 'urn:xccdf:fix:script:javascript', # Javascript (ECMAScript, JScript)
        # 'urn:xccdf:fix:script:tcl', # Tcl and all Tcl-based scripting languages
        # # A URN of this form specifies that the content of the fix element is a
        # # script written in the given language. Executing the script should
        # # bring the target system into compliance with the Rule.
        #
        # 'urn:xccdf:fix:patch:microsoft',
        # 'urn:xccdf:fix:patch:redhat',
        # # A URN of this form specifies that the content of the fix element is a
        # # patch identifier, in proprietary format as defined by the vendor.
    ]

    def __str__(self):
        s = self.system + ':'

        if self.id is not None:
            s += self.id + ':'

        if len(self.check_content_refs) > 0:
            s += str([ref.href + ('' if not hasattr(ref, 'name') else '#' + ref.name) for ref in self.check_content_refs])
        return s

    def fix(self, benchmark, host):
        # TODO check platform applies

        if self.system not in self.SYSTEM_ENUMERATION:
            return False

        # TODO confirm, if reboot needed

        # TODO strategy?

        raise NotImplementedError('fixing is not yet implemented')
