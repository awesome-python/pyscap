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

logger = logging.getLogger(__name__)
class Model(object):
    @staticmethod
    def load(content):
        root = content.getroot()
        from scap.Engine import Engine
        if root.tag.startswith('{' + Engine.namespaces['scap_1_2']):
            from scap.model.scap_1_2.DataStreamCollection import DataStreamCollection
            dsc = DataStreamCollection()
            dsc.from_xml(None, root)
            return dsc
        else:
            logger.critical('Unsupported content with root namespace: ' + str(content.get_root_namespace()))
            sys.exit()

    def __init__(self):
        self.parent = None
        self.element = None
        self.ref_mapping = {}

    def from_xml(self, parent, el, ref_mapping=None):
        self.parent = parent
        self.element = el
        if ref_mapping is not None:
            self.ref_mapping.update(ref_mapping)

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            ref = self.ref_mapping[ref]

        if not self.parent:
            raise RuntimeError("Got to null parent without resolving reference")
        return self.parent.resolve_reference(ref)

    def set_ref_mapping(self, mapping):
        logger.debug('Updating reference mapping with ' + str(mapping))
        self.ref_mapping.update(mapping)

    def to_xml(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
