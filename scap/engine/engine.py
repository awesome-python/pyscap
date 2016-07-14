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

import logging, inspect
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class Engine(object):
    namespaces = {
        'ai_1_1': 'http://scap.nist.gov/schema/asset-identification/1.1',
        'arf_1_1': 'http://scap.nist.gov/schema/asset-reporting-format/1.1',
        'arf_rel_1_0': 'http://scap.nist.gov/specifications/arf/vocabulary/relationships/1.0',
        'cpe_dict_2_0': 'http://cpe.mitre.org/dictionary/2.0',
        'cpe_lang_2_0': 'http://cpe.mitre.org/language/2.0',
        'dc_el_1_1': 'http://purl.org/dc/elements/1.1/',
        'ocil_2_0': 'http://scap.nist.gov/schema/ocil/2.0',
        'oval_common_5': 'http://oval.mitre.org/XMLSchema/oval-common-5',
        'oval_defs_5': 'http://oval.mitre.org/XMLSchema/oval-definitions-5',
        'oval_defs_5_independent': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#independent',
        'oval_defs_5_windows': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'scap_1_2': 'http://scap.nist.gov/schema/scap/source/1.2',
        'rep_core_1_1': 'http://scap.nist.gov/schema/reporting-core/1.1',
        'xccdf_1_1': 'http://checklists.nist.gov/xccdf/1.1',
        'xccdf_1_2': 'http://checklists.nist.gov/xccdf/1.2',
        'xhtml': 'http://www.w3.org/1999/xhtml',
        'xlink': 'http://www.w3.org/1999/xlink',
        'xml_cat': 'urn:oasis:names:tc:entity:xmlns:xml:catalog',
        'xml_dsig_1_0': 'http://scap.nist.gov/schema/xml-dsig/1.0',
        'xml_schema_instance': 'http://www.w3.org/2001/XMLSchema-instance',
        'xmldsig_2000_09': 'http://www.w3.org/2000/09/xmldsig',
    }

    @staticmethod
    def get_engine(content, args):

        root = content.getroot()
        if root.tag.startswith('{' + Engine.namespaces['scap_1_2']):
            from scap.engine.scap_1_2_engine import SCAP1_2Engine
            return SCAP1_2Engine(content, args)
        else:
            # TODO data stream contains supported dictionaries, checklists, and checks
            logger.critical('Unsupported content with root namespace: ' + str(content.get_root_namespace()))
            sys.exit()

    def collect(self, targets):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def report(self):
        logger.error(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
