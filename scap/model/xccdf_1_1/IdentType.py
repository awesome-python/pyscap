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

from scap.model.xs.String import String
import logging

logger = logging.getLogger(__name__)
class IdentType(String):
    MODEL_MAP = {
        'attributes': {
            'system': {'type': 'AnyURI', 'required': True},
            '*': {'ignore': True},
        }
    }

    SYSTEM_ENUMERATION = [
        'http://cve.mitre.org/',
        # MITRE’s Common Vulnerabilities and Exposures – the identifier value
        # should be a CVE number or CVE candidate number.
        'http://cce.mitre.org/',
        # This specifies the Common Configuration Enumeration identifier scheme.
        'http://www.cert.org/',
        # CERT Coordination Center – the identifier value should be a CERT
        # advisory identifier (e.g. “CA-2004-02”).
        'http://www.us-cert.gov/cas/techalerts/',
        # US-CERT technical cyber security alerts – the identifier value should
        # be a technical cyber security alert ID (e.g. “TA05-189A”)
        'http://www.kb.cert.org/',
        # US-CERT vulnerability notes database – the identifier values should be
        # a vulnerability note number (e.g. “709220”).
        'http://iase.disa.mil/IAalerts/',
        # DISA Information Assurance Vulnerability Alerts (IAVA) – the
        # identifier value should be a DOD IAVA identifier.
    ]
