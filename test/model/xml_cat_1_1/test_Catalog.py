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

import pytest
from scap.Model import Model
from scap.model.xml_cat_1_1.Catalog import Catalog
import xml.etree.ElementTree as ET
ET.register_namespace('cat', 'urn:oasis:names:tc:entity:xmlns:xml:catalog')

cat1 = Model.load(None, ET.fromstring('''<cat:catalog xmlns:cat="urn:oasis:names:tc:entity:xmlns:xml:catalog">
    <cat:uri name="name1" uri="uri1"/>
    <cat:uri name="name2" uri="uri2"/>
    <cat:uri name="name3" uri="uri3"/>
</cat:catalog>'''))

def test_parsed():
    assert 'name1' in cat1.entries
    assert 'name2' in cat1.entries
    assert 'name2' in cat1.entries
    assert cat1.entries['name1'] == 'uri1'
    assert cat1.entries['name2'] == 'uri2'
    assert cat1.entries['name3'] == 'uri3'
    assert 'name4' not in cat1.entries

def test_to_dict():
    d = cat1.to_dict()
    assert 'name1' in d
    assert 'name2' in d
    assert 'name2' in d
    assert d['name1'] == 'uri1'
    assert d['name2'] == 'uri2'
    assert d['name3'] == 'uri3'
    assert 'name4' not in d

cat2 = Catalog()
cat2.from_dict({'n1': 'u1', 'n2': 'u2'})
def test_to_xml():
    xml = ET.tostring(cat2.to_xml())
    print xml
    assert xml == '''<cat:catalog xmlns:cat="urn:oasis:names:tc:entity:xmlns:xml:catalog">
    <cat:uri name="n1" uri="u1"/>
    <cat:uri name="n2" uri="u2"/>
</cat:catalog>'''
