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
from scap.model.cpe_2_3.CPE import CPE

class TestCPE:
    def test_from_uri(self):
        cpe = CPE.from_string('cpe:/a:microsoft:internet_explorer')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'microsoft'
        assert cpe.get_value_middle('product') == 'internet_explorer'
        assert cpe.is_value_any('version') == True
        assert cpe.is_value_any('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.is_value_any('target_sw') == True
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('cpe:/a:foo%5cbar:big%24money_manager_2010:2010:u5:~legacy_edition~special~ipod_touch~80gb~other:EN-us')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'foo\\bar'
        assert cpe.get_value_middle('product') == 'big$money_manager_2010'
        assert cpe.get_value_middle('version') == '2010'
        assert cpe.get_value_middle('update') == 'u5'
        assert cpe.get_value_middle('edition') == 'legacy_edition'
        assert cpe.get_value_middle('sw_edition') == 'special'
        assert cpe.get_value_middle('target_sw') == 'ipod_touch'
        assert cpe.get_value_middle('target_hw') == '80gb'
        assert cpe.get_value_middle('other') == 'other'
        assert cpe.get_value_middle('language') == 'EN-us'

        cpe = CPE.from_string('cpe:/a:foo%5cbar:big%24money_manager_2010:2010:u5:~legacy_edition~special~ipod_touch~80gb~other')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'foo\\bar'
        assert cpe.get_value_middle('product') == 'big$money_manager_2010'
        assert cpe.get_value_middle('version') == '2010'
        assert cpe.get_value_middle('update') == 'u5'
        assert cpe.get_value_middle('edition') == 'legacy_edition'
        assert cpe.get_value_middle('sw_edition') == 'special'
        assert cpe.get_value_middle('target_sw') == 'ipod_touch'
        assert cpe.get_value_middle('target_hw') == '80gb'
        assert cpe.get_value_middle('other') == 'other'
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('cpe:/a:foo%5cbar:big%24money_manager_2010:2010:u5:~legacy_edition~special~ipod_touch~80gb~other')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'foo\\bar'
        assert cpe.get_value_middle('product') == 'big$money_manager_2010'
        assert cpe.get_value_middle('version') == '2010'
        assert cpe.get_value_middle('update') == 'u5'
        assert cpe.get_value_middle('edition') == 'legacy_edition'
        assert cpe.get_value_middle('sw_edition') == 'special'
        assert cpe.get_value_middle('target_sw') == 'ipod_touch'
        assert cpe.get_value_middle('target_hw') == '80gb'
        assert cpe.get_value_middle('other') == 'other'
        assert cpe.is_value_any('language') == True

    def test_from_wfn(self):
        cpe = CPE.from_string('wfn:[part="a",vendor="microsoft",product="internet_explorer"]')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'microsoft'
        assert cpe.get_value_middle('product') == 'internet_explorer'
        assert cpe.is_value_any('version') == True
        assert cpe.is_value_any('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.is_value_any('target_sw') == True
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=NA]')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'microsoft'
        assert cpe.get_value_middle('product') == 'internet_explorer'
        assert cpe.get_value_middle('version') == '8.0.6001'
        assert cpe.get_value_middle('update') == 'beta'
        assert cpe.is_value_na('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.is_value_any('target_sw') == True
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?",edition=NA,language=ANY]')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'microsoft'
        assert cpe.get_value_middle('product') == 'internet_explorer'
        assert cpe.get_value_middle('version') == '8.'
        assert cpe.value_ends_with_any('version') == True
        assert cpe.get_value_middle('update') == 'sp'
        assert cpe.get_singles_after_value('update') == 1
        assert cpe.is_value_na('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.is_value_any('target_sw') == True
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('wfn:[part="a",vendor="hp",product="insight_diagnostics",version="7\.4\.0\.1570",sw_edition="online",target_sw="windows_2003",target_hw="x64"]')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'hp'
        assert cpe.get_value_middle('product') == 'insight_diagnostics'
        assert cpe.get_value_middle('version') == '7.4.0.1570'
        assert cpe.is_value_any('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.get_value_middle('sw_edition') == 'online'
        assert cpe.get_value_middle('target_sw') == 'windows_2003'
        assert cpe.get_value_middle('target_hw') == 'x64'
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('wfn:[part="a",vendor="hp",product="openview_network_manager",version="7\.51",update=NA,target_sw="linux"]')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'hp'
        assert cpe.get_value_middle('product') == 'openview_network_manager'
        assert cpe.get_value_middle('version') == '7.51'
        assert cpe.is_value_na('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.get_value_middle('target_sw') == 'linux'
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('wfn:[part="a",vendor="foo\\bar",product="big\$money_2010",sw_edition="special",target_sw="ipod_touch"]')
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'foo\\bar'
        assert cpe.get_value_middle('product') == 'big$money_2010'
        assert cpe.is_value_any('version') == True
        assert cpe.is_value_any('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.get_value_middle('sw_edition') == 'special'
        assert cpe.get_value_middle('target_sw') == 'ipod_touch'
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

    def test_from_fs(self):
        cpe = CPE.from_string('cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*')
        # 'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=ANY,sw_edition=ANY,target_sw=ANY,target_hw=ANY,other=ANY,language=ANY]',
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'microsoft'
        assert cpe.get_value_middle('product') == 'internet_explorer'
        assert cpe.get_value_middle('version') == '8.0.6001'
        assert cpe.get_value_middle('update') == 'beta'
        assert cpe.is_value_any('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.is_value_any('target_sw') == True
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*')
        # 'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?",edition=ANY,sw_edition=ANY,target_sw=ANY,target_hw=ANY,other=ANY,language=ANY]',
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'microsoft'
        assert cpe.get_value_middle('product') == 'internet_explorer'
        assert cpe.get_value_middle('version') == '8.'
        assert cpe.value_ends_with_any('version') == True
        assert cpe.get_value_middle('update') == 'sp'
        assert cpe.get_singles_after_value('update') == 1
        assert cpe.is_value_any('edition') == True
        assert cpe.is_value_any('sw_edition') == True
        assert cpe.is_value_any('target_sw') == True
        assert cpe.is_value_any('target_hw') == True
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('cpe:2.3:a:hp:insight_diagnostics:7.4.0.1570:-:*:*:online:win2003:x64:*')
        # 'wfn:[part="a",vendor="hp",product="insight_diagnostics",version="7\.4\.0\.1570",update=NA,edition=ANY,sw_edition="online",target_sw="win2003",target_hw="x64",other=ANY,language=ANY]',
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'hp'
        assert cpe.get_value_middle('product') == 'insight_diagnostics'
        assert cpe.get_value_middle('version') == '7.4.0.1570'
        assert cpe.is_value_na('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.get_value_middle('sw_edition') == 'online'
        assert cpe.get_value_middle('target_sw') == 'win2003'
        assert cpe.get_value_middle('target_hw') == 'x64'
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True

        cpe = CPE.from_string('cpe:2.3:a:foo\\bar:big\$money:2010:*:*:*:special:ipod_touch:80gb:*')
        # 'wfn:[part="a",vendor="foo\\bar",product="big\$money",version="2010",update=ANY,edition=ANY,sw_edition="special",target_sw="ipod_touch",target_hw="80gb",other=ANY,language=ANY]',
        assert cpe.get_value_middle('part') == 'a'
        assert cpe.get_value_middle('vendor') == 'foo\\bar'
        assert cpe.get_value_middle('product') == 'big$money'
        assert cpe.get_value_middle('version') == '2010'
        assert cpe.is_value_any('update') == True
        assert cpe.is_value_any('edition') == True
        assert cpe.get_value_middle('sw_edition') == 'special'
        assert cpe.get_value_middle('target_sw') == 'ipod_touch'
        assert cpe.get_value_middle('target_hw') == '80gb'
        assert cpe.is_value_any('other') == True
        assert cpe.is_value_any('language') == True


    def test_from_wfn_to_wfn(self):
        tests = [
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=NA]',
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?",edition=NA,language=ANY]',
            'wfn:[part="a",vendor="hp",product="insight_diagnostics",version="7\.4\.0\.1570",sw_edition="online",target_sw="windows_2003",target_hw="x64"]',
            'wfn:[part="a",vendor="hp",product="openview_network_manager",version="7\.51",update=NA,target_sw="linux"]',
            'wfn:[part="a",vendor="foo\\bar",product="big\$money_2010",sw_edition="special",target_sw="ipod_touch"]',
        ]
        for s in tests:
            assert CPE.from_string(s).equal_to(CPE(s)) == True

    def test_from_wfn_to_uri(self):
        tests = {
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=ANY]':
                'cpe:/a:microsoft:internet_explorer:8.0.6001:beta',
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?"]':
                'cpe:/a:microsoft:internet_explorer:8.%02:sp%01',
            'wfn:[part="a",vendor="hp",product="insight_diagnostics",version="7\.4\.0\.1570",update=NA,sw_edition="online",target_sw="win2003",target_hw="x64"]':
                'cpe:/a:hp:insight_diagnostics:7.4.0.1570:-:~~online~win2003~x64~',
            'wfn:[part="a",vendor="hp",product="openview_network_manager",version="7\.51",target_sw="linux"]':
                'cpe:/a:hp:openview_network_manager:7.51::~~~linux~~',
            'wfn:[part="a",vendor="foo\\bar",product="big\$money_manager_2010",sw_edition="special",target_sw="ipod_touch",target_hw="80gb"]':
                'cpe:/a:foo%5cbar:big%24money_manager_2010:::~~special~ipod_touch~80gb~',
        }
        for s in tests.keys():
            assert CPE.from_string(s).to_uri_string() == tests[s]

    def test_from_uri_to_wfn(self):
        assert CPE('cpe:/a:microsoft:internet_explorer:8.0.6001:beta').equal_to(CPE(
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=ANY,language=ANY]')) == True
        assert CPE('cpe:/a:microsoft:internet_explorer:8.%2a:sp%3f').equal_to(CPE(
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.\*",update="sp\?",edition=ANY,language=ANY]')) == True
        assert CPE('cpe:/a:microsoft:internet_explorer:8.%02:sp%01').equal_to(CPE(
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?",edition=ANY,language=ANY]')) == True
        assert CPE('cpe:/a:hp:insight_diagnostics:7.4.0.1570::~~online~win2003~x64~').equal_to(CPE(
            'wfn:[part="a",vendor="hp",product="insight_diagnostics",version="7\.4\.0\.1570",update=ANY,edition=ANY,sw_edition="online",target_sw="win2003",target_hw="x64",other=ANY,language=ANY]')) == True
        assert CPE('cpe:/a:hp:openview_network_manager:7.51:-:~~~linux~~').equal_to(CPE(
            'wfn:[part="a",vendor="hp",product="openview_network_manager",version="7\.51",update=NA,edition=ANY,sw_edition=ANY,target_sw="linux",target_hw=ANY,other=ANY,language=ANY]')) == True
        assert CPE('cpe:/a:foo~bar:big%7emoney_2010').equal_to(CPE(
            'wfn:[part="a",vendor="foo\~bar",product="big\~money_2010",version=ANY,update=ANY,edition=ANY,language=ANY]')) == True

    def test_from_uri_to_uri(self):
        tests = [
            'cpe:/a:microsoft:internet_explorer:8.0.6001:beta',
            'cpe:/a:microsoft:internet_explorer:8.%2a:sp%3f',
            'cpe:/a:microsoft:internet_explorer:8.%02:sp%01',
            'cpe:/a:hp:insight_diagnostics:7.4.0.1570::~~online~win2003~x64~',
            'cpe:/a:hp:openview_network_manager:7.51:-:~~~linux~~',
            'cpe:/a:foo%7ebar:big%7emoney_2010',
            'cpe:/a:foo%5cbar:big%24money_manager_2010:2010:u5:~legacy_edition~special~ipod_touch~80gb~other',
            'cpe:/a:foo%5cbar:big%24money_manager_2010:2010:u5:~legacy_edition~special~ipod_touch~80gb~other:EN-us',
        ]
        for s in tests:
            assert CPE(s).to_uri_string() == s

    def test_from_uri_to_wfn_error(self):
        errors = [
            'cpe:/a:foo%5cbar:big%24money_2010%07:::~~special~ipod_touch~80gb~',
            'cpe:/a:foo:bar:12.%02.1234',
        ]
        for s in errors:
            with pytest.raises(RuntimeError):
                CPE.from_string(s).to_uri_string()

    def test_from_wfn_to_fs(self):
        tests = {
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=ANY]':
                'cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*',
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?",edition=ANY]':
                'cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*',
            'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.\*",update="sp?"]':
                'cpe:2.3:a:microsoft:internet_explorer:8.\*:sp?:*:*:*:*:*:*',
            'wfn:[part="a",vendor="hp",product="insight",version="7\.4\.0\.1570",update=NA,sw_edition="online",target_sw="win2003",target_hw="x64"]':
                'cpe:2.3:a:hp:insight:7.4.0.1570:-:*:*:online:win2003:x64:*',
            'wfn:[part="a",vendor="hp",product="openview_network_manager",version="7\.51",target_sw="linux"]':
                'cpe:2.3:a:hp:openview_network_manager:7.51:*:*:*:*:linux:*:*',
            r'wfn:[part="a",vendor="foo\\bar",product="big\$money_2010",sw_edition="special",target_sw="ipod_touch",target_hw="80gb"]':
                r'cpe:2.3:a:foo\\bar:big\$money_2010:*:*:*:*:special:ipod_touch:80gb:*',
        }
        for s in tests.keys():
            assert CPE.from_string(s).to_fs_string() == tests[s]

    def test_from_fs_to_wfn(self):
        tests = {
            'cpe:2.3:a:microsoft:internet_explorer:8.0.6001:beta:*:*:*:*:*:*':
                'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.0\.6001",update="beta",edition=ANY,sw_edition=ANY,target_sw=ANY,target_hw=ANY,other=ANY,language=ANY]',
            'cpe:2.3:a:microsoft:internet_explorer:8.*:sp?:*:*:*:*:*:*':
                'wfn:[part="a",vendor="microsoft",product="internet_explorer",version="8\.*",update="sp?",edition=ANY,sw_edition=ANY,target_sw=ANY,target_hw=ANY,other=ANY,language=ANY]',
            'cpe:2.3:a:hp:insight_diagnostics:7.4.0.1570:-:*:*:online:win2003:x64:*':
                'wfn:[part="a",vendor="hp",product="insight_diagnostics",version="7\.4\.0\.1570",update=NA,edition=ANY,sw_edition="online",target_sw="win2003",target_hw="x64",other=ANY,language=ANY]',
            r'cpe:2.3:a:foo\\bar:big\$money:2010:*:*:*:special:ipod_touch:80gb:*':
                r'wfn:[part="a",vendor="foo\\bar",product="big\$money",version="2010",update=ANY,edition=ANY,sw_edition="special",target_sw="ipod_touch",target_hw="80gb",other=ANY,language=ANY]',
        }
        for s in tests.keys():
            cpe = CPE.from_string(s)
            assert cpe.to_wfn_string() == tests[s]

    def test_from_fs_to_wfn_errors(self):
        errors = [
            'cpe:2.3:a:hp:insight_diagnostics:7.4.*.1570:*:*:*:*:*:*',
        ]
        with pytest.raises(RuntimeError):
            for s in errors:
                CPE.from_string(s)

    def test_value_contains_wildcard_true(self):
        val = CPE.Value()
        val.from_wfn('"?foo"')
        assert val.contains_wildcard() == True
        val.from_wfn('"??foo"')
        assert val.contains_wildcard() == True
        val.from_wfn('"*bar"')
        assert val.contains_wildcard() == True
        val.from_wfn('"foo?"')
        assert val.contains_wildcard() == True
        val.from_wfn('"foo??"')
        assert val.contains_wildcard() == True
        val.from_wfn('"bar*"')
        assert val.contains_wildcard() == True

    def test_value_contains_wildcard_false(self):
        val = CPE.Value()
        val.from_wfn('"foo"')
        assert val.contains_wildcard() == False
        val.from_wfn('"foo\?"')
        assert val.contains_wildcard() == False
        val.from_wfn('"\*bar"')
        assert val.contains_wildcard() == False

    def test_value_matches_true(self):
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='foo')) == True          # 0 match
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='1foo')) == True         # full match
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='\?foo')) == True        # quoted match

        # double ?
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='foo')) == True         # 0 match
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='1foo')) == True        # 0 full match
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='12foo')) == True       # full match
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='\?foo')) == True       # 0 full match
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='\?\?foo')) == True     # full match

        assert CPE.Value(fs='*bar').matches(CPE.Value(fs='bar')) == True          # 0 match
        assert CPE.Value(fs='*bar').matches(CPE.Value(fs='blahbar')) == True      # full match
        assert CPE.Value(fs='*bar').matches(CPE.Value(fs='blah\?bar')) == True    # full match + quoted

        assert CPE.Value(fs='foo?').matches(CPE.Value(fs='foo')) == True          # 0 match
        assert CPE.Value(fs='foo?').matches(CPE.Value(fs='foo1')) == True         # full match
        assert CPE.Value(fs='foo?').matches(CPE.Value(fs='foo\?')) == True        # quoted match

        # double ?
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo')) == True         # 0 match
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo1')) == True        # 0 full match
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo12')) == True       # full match
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo\?')) == True       # 0 full match
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo\?\?')) == True     # full match

    def test_value_matches_false(self):
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='fo')) == False
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='12foo')) == False
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='\?\?foo')) == False
        assert CPE.Value(fs='?foo').matches(CPE.Value(fs='foo1')) == False

        # double ?
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='fo')) == False
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='123foo')) == False
        assert CPE.Value(fs='??foo').matches(CPE.Value(fs='foo12')) == False

        assert CPE.Value(fs='*bar').matches(CPE.Value(fs='ba')) == False
        assert CPE.Value(fs='*bar').matches(CPE.Value(fs='blah\?ba')) == False

        assert CPE.Value(fs='foo?').matches(CPE.Value(fs='fo')) == False
        assert CPE.Value(fs='foo?').matches(CPE.Value(fs='foo12')) == False
        assert CPE.Value(fs='foo?').matches(CPE.Value(fs='foo\?\?')) == False

        # double ?
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='fo')) == False
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo123')) == False
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='\?foo')) == False
        assert CPE.Value(fs='foo??').matches(CPE.Value(fs='foo\?\?\?')) == False
