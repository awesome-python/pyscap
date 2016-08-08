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

logger = logging.getLogger(__name__)
class ArtifactResultType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://scap.nist.gov/schema/ocil/2.0}submitter': {'class': 'UserType'},
        }
    }
    def __init__(self):
        super(ArtifactResultType, self).__init__()

        self.artifact_ref = None
        self.timestamp = None

        self.artifact_value = None
        self.provider = None
        self.submitter = None

    def parse_attribute(self, name, value):
        if name == 'artifact_ref':
            self.artifact_ref = value
        elif name == 'timestamp':
            self.timestamp = value
        else:
            return super(ArtifactResultType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}artifact_value':
            self.artifact_value = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}provider':
            self.provider = sub_el.text
        elif sub_el.tag == '{http://scap.nist.gov/schema/ocil/2.0}submitter':
            self.submitter = Model.load(self, sub_el)
        else:
            return super(ArtifactResultType, self).parse_element(sub_el)
        return True
