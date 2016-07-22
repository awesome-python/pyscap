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

from scap.model.Simple import Simple
import logging

logger = logging.getLogger(__name__)
class DataStream(Simple):
    def __init__(self):
        super(DataStream, self).__init__()

        self.checklists = {}
        self.checks = []

        self.required_attributes.extend([
            'id',
            'use-case',
            'scap-version',
            'timestamp',
        ])
        self.ignore_attributes.extend([
            'use-case',
            'scap-version',
            'timestamp',
        ])
        self.ignore_sub_elements.extend([
            '{http://scap.nist.gov/schema/scap/source/1.2}dictionaries',
            '{http://scap.nist.gov/schema/scap/source/1.2}extended-components',
        ])

    def parse_comp_ref(self, sub_el, comp_ref_el):
        if comp_ref_el.tag != '{http://scap.nist.gov/schema/scap/source/1.2}component-ref':
            logger.critical(sub_el.tag + ' element can only contain component-ref elements')
            import sys
            sys.exit()
        ref_mapping = None
        href = comp_ref_el.attrib['{http://www.w3.org/1999/xlink}href']
        for cat_el in comp_ref_el:
            if cat_el.tag != '{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog':
                logger.critical('component-ref element can only contain xml-cat:catalog elements')
                import sys
                sys.exit()
            logger.debug('Loading catalog for ' + href)
            from scap.model.xml_cat.Catalog import Catalog
            cat = Catalog()
            cat.from_xml(self, cat_el)
            ref_mapping = cat.to_dict()
        comp_el = self.parent.resolve_reference(href)

        return comp_el, ref_mapping

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}checklists':
            for comp_ref_el in sub_el:
                comp_el, ref_mapping = self.parse_comp_ref(sub_el, comp_ref_el)
                if comp_el.tag == '{http://checklists.nist.gov/xccdf/1.2}Benchmark':
                    from scap.model.xccdf_1_2.Benchmark import Benchmark
                    comp = Benchmark()
                    comp.from_xml(self, comp_el, ref_mapping=ref_mapping)
                elif comp_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}ocil':
                    from scap.model.ocil_2_0.OCIL import OCIL
                    comp = OCIL()
                    comp.from_xml(self, comp_el, ref_mapping=ref_mapping)
                else:
                    logger.critical('unknown checklists component: ' + comp_el.tag + ' for ref: ' + comp_ref_el.attrib['{http://www.w3.org/1999/xlink}href'])
                    import sys
                    sys.exit()
                self.checklists[comp.id] = comp
        elif sub_el.tag == '{http://scap.nist.gov/schema/scap/source/1.2}checks':
            for comp_ref_el in sub_el:
                comp_el, ref_mapping = self.parse_comp_ref(sub_el, comp_ref_el)
                if comp_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions':
                    from scap.model.oval_defs_5.OVALDefinitions import OVALDefinitions
                    comp = OVALDefinitions()
                    comp.from_xml(self, comp_el, ref_mapping=ref_mapping)
                elif comp_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}ocil':
                    from scap.model.ocil_2_0.OCIL import OCIL
                    comp = OCIL()
                    comp.from_xml(self, comp_el, ref_mapping=ref_mapping)
                else:
                    logger.critical('unknown checks component: ' + comp_el.tag + ' for ref: ' + comp_ref_el.attrib['{http://www.w3.org/1999/xlink}href'])
                    import sys
                    sys.exit()
                self.checks.append(comp)
        else:
            return super(DataStream, self).parse_sub_el(sub_el)
        return True
