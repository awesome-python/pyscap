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

from scap.model.xccdf_1_2.GroupRuleCommon import GroupRuleCommon
import logging

logger = logging.getLogger(__name__)
class Rule(GroupRuleCommon):
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

    def __init__(self):
        super(Rule, self).__init__()
        self.checks = {}

        self.ignore_attributes.extend([
            'role',
            'severity',
            'multiple',
        ])
        self.ignore_sub_elements.extend([
            '{http://checklists.nist.gov/xccdf/1.2}ident',
            '{http://checklists.nist.gov/xccdf/1.2}impact-metric',
            '{http://checklists.nist.gov/xccdf/1.2}profile-note',
            '{http://checklists.nist.gov/xccdf/1.2}fixtext',
            '{http://checklists.nist.gov/xccdf/1.2}fix',
            '{http://checklists.nist.gov/xccdf/1.2}signature',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}complex-check':
            from scap.model.xccdf_1_2.ComplexCheck import ComplexCheck
            check = ComplexCheck()
            check.from_xml(self, sub_el)
            self.checks[None] = check
        elif sub_el.tag == '{http://checklists.nist.gov/xccdf/1.2}check':
            from scap.model.xccdf_1_2.Check import Check
            check = Check()
            check.from_xml(self, sub_el)
            if 'selector' in sub_el.attrib:
                self.checks[sub_el.attrib['selector']] = check
            else:
                self.checks[None] = check
        else:
            return super(Rule, self).parse_sub_el(sub_el)
        return True
