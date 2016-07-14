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

import re, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class CPE(object):
    class Value(object):
        def __init__(self, wfn = None, uri = None, fs = None):
            self.ANY = True
            self.NA = False
            self.any_before = False
            self.singles_before = 0
            self.middle = None
            self.any_after = False
            self.singles_after = 0

            if wfn:
                self.from_wfn(wfn)
            elif uri:
                self.from_uri(uri)
            elif fs:
                self.from_fs(fs)

        def __eq__(self, other):
            if self.ANY != other.ANY:
                return False
            if self.NA != other.NA:
                return False
            if self.any_before != other.any_before:
                return False
            if self.singles_before != other.singles_before:
                return False
            if self.middle is None:
                if not other.middle is None:
                    return False
                # else both none
            else:
                if other.middle is None:
                    return False
                # spec says to always be case insensitive
                if self.middle.lower() != other.middle.lower():
                    return False
            if self.any_after != other.any_after:
                return False
            if self.singles_after != other.singles_after:
                return False
            return True

        def __ne__(self, other):
            return not self.__eq__(other)

        ###### WFN ######

        WFN_QUOTE_MAP = {
            '!': '\\!',
            '"': '\\"',
            '#': '\\#',
            '$': '\\$',
            '%': '\\%',
            '&': '\\&',
            '\'': '\\\'',
            '(': '\\(',
            ')': '\\)',
            '+': '\\+',
            ',': '\\,',
            '.': '\\.',
            '/': '\\/',
            ':': '\\:',
            ';': '\\;',
            '<': '\\<',
            '=': '\\=',
            '>': '\\>',
            '@': '\\@',
            '[': '\\[',
            ']': '\\]',
            '^': '\\^',
            '`': '\\`',
            '{': '\\{',
            '|': '\\|',
            '}': '\\}',
            '~': '\\~',
            '-': '\\-',
            '*': '\\*',
            '?': '\\?',
        }
        WFN_UNQUOTE_MAP = {v: k for k, v in WFN_QUOTE_MAP.items()}
        WFN_UNQUOTE_MAP['\\\\'] = '\\'
        WFN_QUOTE_MAP[' '] = '_'

        def to_wfn(self):
            # special values
            if self.ANY:
                return 'ANY'
            if self.NA:
                return 'NA'

            # replace special chars
            value = self.middle
            for k,v in self.WFN_QUOTE_MAP.items():
                value = value.replace(k, v)

            # attach the wildcards
            if self.any_before:
                value = '*' + value
            elif self.singles_before > 0:
                value = ('?' * self.singles_before) + value
            if self.any_after:
                value = value + '*'
            elif self.singles_after > 0:
                value = value + ('?' * self.singles_after)

            return '"' + value + '"'

        def from_wfn(self, value):
            # special values
            if value == 'ANY':
                self.ANY = True
                return
            self.ANY = False
            if value == 'NA':
                self.NA = True
                return

            # strip quotes
            value = value[1:-1]

            # parse wildcards
            if value.startswith('*'):
                self.any_before = True
                value = value[1:]
            while value.startswith('?'):
                self.singles_before += 1
                value = value[1:]
            if value[-1] == '*' and value[-2] != '\\':
                self.any_after = True
                value = value[:-1]
            while value[-1] == '?' and value[-2] != '\\':
                self.singles_after += 1
                value = value[:-1]

            # convert escaped chars
            for k,v in self.WFN_UNQUOTE_MAP.items():
                value = value.replace(k,v)

            self.middle = value

        ###### URI ######

        URI_QUOTE_MAP = {
            '\\': '%5c',
            '!': '%21',
            '"': '%22',
            '#': '%23',
            '$': '%24',
            '&': '%26',
            '\'': '%27',
            '(': '%28',
            ')': '%29',
            '*': '%2a',
            '+': '%2b',
            ',': '%2c',
            '/': '%2f',
            ':': '%3a',
            ';': '%3b',
            '<': '%3c',
            '=': '%3d',
            '>': '%3e',
            '?': '%3f',
            '@': '%40',
            '[': '%5b',
            ']': '%5d',
            '^': '%5e',
            '`': '%60',
            '{': '%7b',
            '|': '%7c',
            '}': '%7d',
            '~': '%7e',
            '%': '%25',
        }
        URI_UNQUOTE_MAP = {v: k for k, v in URI_QUOTE_MAP.items()}

        def to_uri(self):
            # special values
            if self.ANY:
                return ''
            if self.NA:
                return '-'

            # replace special chars
            value = self.middle
            for k,v in self.URI_QUOTE_MAP.items():
                value = value.replace(k, v)

            # attach the wildcards
            if self.any_before:
                value = '%02' + value
            elif self.singles_before > 0:
                value = ('%01' * self.singles_before) + value
            if self.any_after:
                value = value + '%02'
            elif self.singles_after > 0:
                value = value + ('%01' * self.singles_after)

            return value

        def from_uri(self, value):
            # special values
            if value == '':
                self.ANY = True
                return
            self.ANY = False
            if value == '-':
                self.NA = True
                return

            # parse wildcards
            if value.startswith('%02'):
                self.any_before = True
                value = value[3:]
            while value.startswith('%01'):
                self.singles_before += 1
                value = value[3:]
            if value.endswith('%02'):
                self.any_after = True
                value = value[:-3]
            while value.endswith('%01'):
                self.singles_after += 1
                value = value[:-3]

            # convert escaped chars
            i = 0
            while i < len(value):
                if value[i] == '%':
                    quoted = value[i:i+3]
                    if quoted not in self.URI_UNQUOTE_MAP:
                        raise RuntimeError('Unable to unquote sequence ' + quoted)
                    value = value.replace(quoted, self.URI_UNQUOTE_MAP[quoted])
                    i += 3
                else:
                    i += 1

            self.middle = value

        ###### FS ######

        FS_QUOTE_MAP = {
            '!': '\\!',
            '"': '\\"',
            '#': '\\#',
            '$': '\\$',
            '%': '\\%',
            '&': '\\&',
            '\'': '\\\'',
            '(': '\\(',
            ')': '\\)',
            '+': '\\+',
            ',': '\\,',
            '/': '\\/',
            ':': '\\:',
            ';': '\\;',
            '<': '\\<',
            '=': '\\=',
            '>': '\\>',
            '@': '\\@',
            '[': '\\[',
            ']': '\\]',
            '^': '\\^',
            '`': '\\`',
            '{': '\\{',
            '|': '\\|',
            '}': '\\}',
            '~': '\\~',
            '*': '\\*',
            '?': '\\?',
        }
        FS_UNQUOTE_MAP = {v: k for k, v in FS_QUOTE_MAP.items()}
        # don't want to unquote ' '
        FS_QUOTE_MAP[' '] = '_'

        def to_fs(self):
            # special values
            if self.ANY:
                return '*'
            if self.NA:
                return '-'

            # replace special chars
            value = self.middle
            # do \ first so we don't double escape the other replacements
            value = self.middle.replace('\\', '\\\\')
            for k,v in self.FS_QUOTE_MAP.items():
                value = value.replace(k, v)

            # attach the wildcards
            if self.any_before:
                value = '*' + value
            elif self.singles_before > 0:
                value = ('?' * self.singles_before) + value
            if self.any_after:
                value = value + '*'
            elif self.singles_after > 0:
                value = value + ('?' * self.singles_after)

            return value

        def from_fs(self, value):
            if value == '*':
                self.ANY = True
                return
            self.ANY = False
            if value == '-':
                self.NA = True
                return

            # parse wildcards
            if value.startswith('*'):
                self.any_before = True
                value = value[1:]
            while value.startswith('?'):
                self.singles_before += 1
                value = value[1:]
            if value[-1] == '*' and value[-2] != '\\':
                self.any_after = True
                value = value[:-1]
            while value[-1] == '?' and value[-2] != '\\':
                self.singles_after += 1
                value = value[:-1]

            # convert escaped chars
            for k,v in self.FS_UNQUOTE_MAP.items():
                value = value.replace(k, v)

            self.middle = value

        ###### Relations ######

        def contains_wildcard(self):
            return self.any_before or self.singles_before > 0 or self.any_after or self.singles_after > 0

        def compare(self, other):
            if self.__eq__(other):
                return CPE.EQUAL
            elif self.ANY:
                if other.contains_wildcard():
                    return CPE.UNDEFINED
                else:
                    return CPE.SUPERSET
            elif self.NA:
                if other.ANY:
                    return CPE.SUBSET
                elif other.contains_wildcard():
                    return CPE.UNDEFINED
                else:
                    return CPE.DISJOINT
            elif self.contains_wildcard():
                if other.ANY:
                    return CPE.SUBSET
                elif other.NA:
                    return CPE.DISJOINT
                elif other.contains_wildcard():
                    return CPE.UNDEFINED
                else:
                    if self.matches(other):
                        return CPE.SUPERSET
                    else:
                        return CPE.DISJOINT
            else:
                if other.ANY:
                    return CPE.SUBSET
                elif other.NA:
                    return CPE.DISJOINT
                elif other.contains_wildcard():
                    return CPE.UNDEFINED
                else:
                    return CPE.DISJOINT

        def matches(self, other):
            other_middle = other.middle[:]
            if self.any_before:
                middle_idx = other_middle.find(self.middle)
                if middle_idx == -1:
                    logger.debug('self.middle not found in other_middle ')
                    return False
                other_middle = other_middle[middle_idx + len(self.middle):]
            else:
                match_single_start = self.singles_before
                while match_single_start > 0:
                    if other_middle.startswith(self.middle):
                        break
                    elif other_middle[0] == '\\':
                        other_middle = other_middle[2:]
                    else:
                        other_middle = other_middle[1:]
                    match_single_start -= 1
                if not other_middle.startswith(self.middle):
                    logger.debug('other_middle ' + other_middle + ' does not start with self.middle ' + self.middle)
                    return False
                other_middle = other_middle[len(self.middle):]
            if self.any_after or len(other_middle) == 0:
                logger.debug('match: any_end or other_middle is empty')
                return True
            match_single_end = self.singles_after
            while match_single_end > 0:
                if other_middle == '':
                    logger.debug('match: other_middle is empty')
                    return True
                elif len(other_middle) > 1 and other_middle[-2] == '\\':
                    other_middle = other_middle[:-2]
                else:
                    other_middle = other_middle[:-1]
                match_single_end -= 1
            if len(other_middle) > 0:
                logger.debug('other_middle is not empty')
                return False
            else:
                logger.debug('match: other_middle is consumed')
                return True

        def set(self, value):
            self.ANY = False
            self.any_before = False
            self.singles_before = 0
            self.middle = value
            self.singles_after = 0
            self.any_after = False

    INDEX = [
        'part',
        'vendor',
        'product',
        'version',
        'update',
        'edition',
        'sw_edition',
        'target_sw',
        'target_hw',
        'other',
        'language',
    ]

    @staticmethod
    def from_string(s):
        cpe = CPE()
        if s.startswith('wfn:'):
            cpe.from_wfn_string(s)
        elif s.startswith('cpe:2.3:'):
            cpe.from_fs_string(s)
        elif s.startswith('cpe:/'):
            cpe.from_uri_string(s)
        else:
            raise RuntimeError('Could not parse CPE from ' + s)
        return cpe

    def __init__(self, s = None):
        self.values = {}
        for k in self.INDEX:
            self.values[k] = CPE.Value()

        if isinstance(s, basestring):
            if s.startswith('wfn:'):
                self.from_wfn_string(s)
            elif s.startswith('cpe:2.3:'):
                self.from_fs_string(s)
            elif s.startswith('cpe:/'):
                self.from_uri_string(s)
            else:
                raise RuntimeError('Could not parse CPE from ' + s)

    def is_value_any(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].ANY

    def is_value_na(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].NA

    def value_starts_with_any(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].any_before

    def value_starts_with_singles(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].singles_before > 0

    def get_singles_before_value(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].singles_before

    def get_value_middle(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].middle

    def value_ends_with_any(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].any_after

    def value_ends_with_singles(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].singles_after > 0

    def get_singles_after_value(self, name):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        return self.values[name].singles_after

    def set_value(self, name, value):
        if name not in CPE.INDEX:
            raise RuntimeError('Invalid component name: ' + name)
        self.values[name].set(value)

    ####### WFN #######
    def from_wfn_string(self, s):
        # strip off wfn:[ and ]
        s = s[5:-1]

        i = 0
        name = ''
        value = ''
        in_name = True
        while i < len(s):
            if s[i] == ',':
                # value finished
                self.values[name].from_wfn(value)
                in_name = True
                name = ''
                value = ''
            elif s[i] == '=':
                # name finished
                if name not in CPE.INDEX:
                    raise RuntimeError('Invalid component name: ' + name)
                in_name = False
            elif in_name:
                name += s[i]
            else:
                value += s[i]
            i += 1
        self.values[name].from_wfn(value)

    def to_wfn_string(self):
        comps = []
        for k in self.INDEX:
            if self.values[k].ANY:
                comps.append("{0}=ANY".format(k))
            elif self.values[k].NA:
                comps.append("{0}=NA".format(k))
            else:
                comps.append("{0}={1}".format(k, self.values[k].to_wfn()))
        return 'wfn:[' + ','.join(comps) + ']'

    ####### URI #######
    COMP_INDEX = [
        'part',
        'vendor',
        'product',
        'version',
        'update',
        'edition',
        'language',
    ]

    EXT_COMP_INDEX = [
        'edition',
        'sw_edition',
        'target_sw',
        'target_hw',
        'other',
    ]

    def from_uri_string(self, s):
        s = s[5:]

        j,i,k = (0,0,0)
        value = ''
        ext_edition = False
        extended = False
        while i < len(s):
            c = s[i]
            if c == '\\':
                if i == len(s) - 1:
                    # can't have \ as last char
                    raise RuntimeError('Invalid URI CPE string: ' + s)
                value += '\\' + s[i + 1]
                i += 2
            elif c == ':':
                if extended:
                    self.values[CPE.EXT_COMP_INDEX[k]].from_uri(value)
                    extended = False
                else:
                    self.values[CPE.COMP_INDEX[j]].from_uri(value)
                value = ''
                j += 1
                i += 1
            elif c == '~':
                if extended:
                    self.values[CPE.EXT_COMP_INDEX[k]].from_uri(value)
                    value = ''
                    k += 1
                    i += 1
                elif CPE.COMP_INDEX[j] == 'edition':
                    # parse the rest of the string as extended
                    extended = True
                    i += 1
                else:
                    value += c
                    i += 1
            else:
                value += c
                i += 1
        if value != '':
            if extended:
                self.values[CPE.EXT_COMP_INDEX[k]].from_uri(value)
            else:
                self.values[CPE.COMP_INDEX[j]].from_uri(value)

    def to_uri_string(self):
        s = 'cpe:/'

        # remove the null comps from the end by going backwards & then reversing the comps
        reverse_comps = self.COMP_INDEX[:]
        reverse_comps.reverse()

        # check if we will need to produce extended components
        all_ext_any = True
        ext_comps = []
        for c in self.EXT_COMP_INDEX[1:]:
            if not self.values[c].ANY:
                all_ext_any = False
            ext_comps.append(self.values[c].to_uri())

        comps = []
        for comp in reverse_comps:
            if comp == 'edition' and not all_ext_any:
                # replace edition with packed
                comps.append('~' + self.values['edition'].to_uri() + '~' + '~'.join(ext_comps))
            elif self.values[comp].ANY and len(comps) == 0:
                # skip this component
                continue
            else:
                comps.append(self.values[comp].to_uri())

        comps.reverse()
        return s + ':'.join(comps)

    ####### FS #######
    FS_INDEX = [
        'part',
        'vendor',
        'product',
        'version',
        'update',
        'edition',
        'language',
        'sw_edition',
        'target_sw',
        'target_hw',
        'other',
    ]

    def from_fs_string(self, s):
        s = s[8:]

        comp = ''
        j = 0
        for i in range(len(s)):
            if s[i] == ':':
                if i == 0:
                    raise RuntimeError('CPE FS cannot start with a :')

                if s[i - 1] == '\\':
                    comp += '\\:'
                else:
                    self.values[CPE.FS_INDEX[j]].from_fs(comp)
                    comp = ''
                    j += 1
            else:
                comp += s[i]
        self.values[CPE.FS_INDEX[j]].from_fs(comp)

        if j + 1 != 11:
            raise RuntimeError('Invalid CPE FS: ' + s)

    def to_fs_string(self):
        comps = []
        for k in self.FS_INDEX:
            # omit Nones
            if self.values[k].ANY:
                comps.append('*')
            elif self.values[k].NA:
                comps.append('-')
            else:
                comps.append(self.values[k].to_fs())
        return 'cpe:2.3:' + ':'.join(comps)

    ####### Relations #######9
    class Relation(object):
        def __init__(self, name):
            self.name = name
    EQUAL = Relation('EQUAL')
    SUPERSET = Relation('SUPERSET')
    SUBSET = Relation('SUBSET')
    DISJOINT = Relation('DISJOINT')
    UNDEFINED = Relation('UNDEFINED')

    def compare(self, other):
        r = {}
        for name in self.INDEX:
            r[name] = self.values[name].compare(other.values[name])
        return r

    def superset_of(self, target):
        relations = self.compare(target)
        for name in self.INDEX:
            if relations[name] != CPE.SUPERSET and relations[name] != CPE.EQUAL:
                logger.debug('Relation between ' + name + ' values is ' + relations[name].name)
                return False
        return True

    def subset_of(self, target):
        relations = self.compare(target)
        for name in self.INDEX:
            if relations[name] != CPE.SUBSET and relations[name] != CPE.EQUAL:
                logger.debug('Relation between ' + name + ' values is ' + relations[name].name)
                return False
        return True

    def equal_to(self, target):
        relations = self.compare(target)
        for name in self.INDEX:
            if relations[name] != CPE.EQUAL:
                logger.debug('Relation between ' + name + ' values is ' + relations[name].name)
                return False
        return True

    def disjoint_with(self, target):
        relations = self.compare(target)
        for name in self.INDEX:
            if relations[name] == CPE.DISJOINT:
                logger.debug('Disjoint on ' + name + ' value')
                return True
        return False

    def matches(self, target):
        return self.superset_of(target)
