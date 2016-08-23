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
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}security_principle': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seassignprimarytokenprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seauditprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sebackupprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sechangenotifyprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreateglobalprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatepagefileprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatepermanentprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatesymboliclinkprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}secreatetokenprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedebugprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seenabledelegationprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seimpersonateprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seincreasebasepriorityprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seincreasequotaprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seincreaseworkingsetprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seloaddriverprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}selockmemoryprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}semachineaccountprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}semanagevolumeprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seprofilesingleprocessprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serelabelprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seremoteshutdownprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serestoreprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesecurityprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seshutdownprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesyncagentprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesystemenvironmentprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesyncagentprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesystemprofileprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sesystemtimeprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setakeownershipprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setcbprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setimezoneprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seundockprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seunsolicitedinputprivilege': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sebatchlogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seinteractivelogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}senetworklogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seremoteinteractivelogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}seservicelogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenybatchLogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenyinteractivelogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenynetworklogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenyremoteInteractivelogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sedenyservicelogonright': {'class': 'oval_defs_5.EntityStateStringType'},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}setrustedcredmanaccessnameright': {'class': 'oval_defs_5.EntityStateStringType'},
        }
    }
