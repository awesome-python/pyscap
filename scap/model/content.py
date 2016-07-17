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

import logging
from scap.engine.engine import Engine

logger = logging.getLogger(__name__)
class Content(object):
    @staticmethod
    def load(content):
        root = content.getroot()
        if root.tag.startswith('{' + Engine.namespaces['scap_1_2']):
            from scap.model.scap_1_2.data_stream_collection import DataStreamCollection
            return DataStreamCollection(root)
            # TODO data stream contains supported dictionaries, checklists, and checks
        else:
            logger.critical('Unsupported content with root namespace: ' + str(content.get_root_namespace()))
            sys.exit()

    def __init__(self, parent, el):
        self.parent = parent
        self.element = el
        self.ref_mapping = {}

    def resolve_reference(self, ref):
        if not self.parent:
            raise RuntimeError("Got to null parent without resolving reference")
        return self.parent.resolve_reference(ref)

    def set_ref_mapping(self, mapping):
        self.ref_mapping.update(mapping)

    def select_rules(self, args):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
