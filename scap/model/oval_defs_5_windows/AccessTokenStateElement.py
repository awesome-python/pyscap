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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)

class AccessTokenStateElement(StateType)::
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'accesstoken_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_principle',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seassignprimarytokenprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seauditprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sebackupprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sechangenotifyprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreateglobalprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatepagefileprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatepermanentprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatesymboliclinkprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatetokenprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedebugprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seenabledelegationprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seimpersonateprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seincreasebasepriorityprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seincreasequotaprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seincreaseworkingsetprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seloaddriverprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}selockmemoryprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}semachineaccountprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}semanagevolumeprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seprofilesingleprocessprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serelabelprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seremoteshutdownprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serestoreprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesecurityprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seshutdownprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesyncagentprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesystemenvironmentprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesyncagentprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesystemprofileprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesystemtimeprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setakeownershipprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setcbprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setimezoneprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seundockprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seunsolicitedinputprivilege',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sebatchlogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seinteractivelogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}senetworklogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seremoteinteractivelogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seservicelogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenybatchLogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenyinteractivelogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenynetworklogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenyremoteInteractivelogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenyservicelogonright',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setrustedcredmanaccessnameright',
        }
    }
