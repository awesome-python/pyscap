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
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Check(Model):
    class Result(object):
        PASS = 'pass' # [P] The target system or system component satisfied all the conditions of the <xccdf:Rule>.
        FAIL = 'fail' # [F] The target system or system component did not satisfy all the conditions of the
        # <xccdf:Rule>.
        ERROR = 'error' # [E] The checking engine could not complete the evaluation, therefore the status of the target's
        # compliance with the <xccdf:Rule> is not certain. This could happen, for example, if a testing
        # tool was run with insufficient privileges and could not gather all of the necessary information.
        UNKNOWN = 'unknown' # [U] The testing tool encountered some problem and the result is unknown. For example, a result of
        # 'unknown' might be given if the testing tool was unable to interpret the output of the checking
        # engine (the output has no meaning to the testing tool).
        NOT_APPLICABLE = 'notapplicable' # [N] The <xccdf:Rule> was not applicable to the target of the test. For example, the
        # <xccdf:Rule> might have been specific to a different version of the target OS, or it might
        # have been a test against a platform feature that was not installed.
        NOT_CHECKED = 'notchecked' # [K] The <xccdf:Rule> was not evaluated by the checking engine. This status is designed for
        # <xccdf:Rule> elements that have no <xccdf:check> elements or that correspond to an
        # unsupported checking system. It may also correspond to a status returned by a checking
        # engine if the checking engine does not support the indicated check code.
        NOT_SELECTED = 'notselected' # [S] The <xccdf:Rule> was not selected in the benchmark.
        INFORMATIONAL = 'informational' # [I] The <xccdf:Rule> was checked, but the output from the checking engine is simply
        # information for auditors or administrators; it is not a compliance category. This status value is
        # designed for <xccdf:Rule> elements whose main purpose is to extract information from the
        # target rather than test the target.
        FIXED = 'fixed' # [X] The <xccdf:Rule> had failed, but was then fixed (possibly by a tool that can automatically
        # apply remediation, or possibly by the human auditor).

    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        if 'id' in el.attrib:
            self.id = el.attrib['id']

        supported = [
            Engine.namespaces['oval_defs_5'],
            Engine.namespaces['ocil_2_0'],
            Engine.namespaces['ocil_2'],
        ]
        if el.attrib['system'] not in supported:
            raise NotImplementedError('Check system ' + el.attrib['system'] + ' is not implemented')

        if 'negate' in el.attrib and el.attrib['negate'] == 'true':
            self.negate = True
        else:
            self.negate = False

        # don't need selector

        if 'multi-check' in el.attrib and el.attrib['multi-check'] == 'true':
            self.multi_check = True
        else:
            self.multi_check = False

        self.check_content = None
        for check_el in el:
            if not check_el.tag.startswith('{' + Engine.namespaces['xccdf_1_2'] + '}'):
                raise RuntimeError('Unknown tag in check: ' + check_el.tag)
            tag = check_el.tag[len('{' + Engine.namespaces['xccdf_1_2'] + '}'):]
            if tag == 'check-export':
                pass
            elif tag == 'check-content-ref':
                content_el = self.resolve_reference(check_el.attrib['href'])
                if not content_el.tag.startswith('{' + el.attrib['system']):
                    raise RuntimeError('Check system does not match loaded reference')
                if el.attrib['system'] == Engine.namespaces['oval_defs_5']:
                    from scap.model.oval_defs_5.OVALDefinitions import OVALDefinitions
                    self.check_content = OVALDefinitions()
                    self.check_content.from_xml(self, content_el)
                    # TODO need to specify def name
                elif el.attrib['system'] == Engine.namespaces['ocil_2_0'] or el.attrib['system'] == Engine.namespaces['ocil_2']:
                    from scap.model.ocil_2_0.OCIL import OCIL
                    self.check_content = OCIL()
                    self.check_content.from_xml(self, content_el)
                    # TODO need to specify using name
                else:
                    raise RuntimeError('Unknown check content type: ' + el.attrib['system'])
            else:
                raise NotImplementedError(tag + ' elements are not implemented for checks')
        if self.check_content is None:
            logger.critical('Check for rule ' + parent.id + ' could not be loaded')
            import sys
            sys.exit()
