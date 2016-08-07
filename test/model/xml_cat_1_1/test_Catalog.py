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
import xml.etree.ElementTree as ET

cat = Model.load(None, ET.fromstring('''<?xml version="1.0" encoding="UTF-8"?>
<cat:catalog xmlns:cat="urn:oasis:names:tc:entity:xmlns:xml:catalog">
    <cat:uri name="name1" uri="uri1"/>
    <cat:uri name="name2" uri="uri2"/>
    <cat:uri name="name3" uri="uri3"/>
</cat:catalog>'''))

def test_parsed():
    assert 'name1' in cat.entries
    assert 'name2' in cat.entries
    assert 'name2' in cat.entries
    assert cat.entries['name1'] == 'uri1'
    assert cat.entries['name2'] == 'uri2'
    assert cat.entries['name3'] == 'uri3'
    assert 'name4' not in cat.entries

def test_to_dict():
    d = cat.to_dict()
    assert 'name1' in d
    assert 'name2' in d
    assert 'name2' in d
    assert d['name1'] == 'uri1'
    assert d['name2'] == 'uri2'
    assert d['name3'] == 'uri3'
    assert 'name4' not in d
