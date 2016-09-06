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
class Checker(object):
    @staticmethod
    def load(host, content, parent, args=None):
        model_namespace = content.__class__.__module__.split('.')[2]
        collector_module = 'scap.checker.' + model_namespace + '.' + content.__class__.__name__
        # try to load the collector's module
        import sys, importlib
        if collector_module not in sys.modules:
            logger.debug('Loading module ' + collector_module)
            import importlib
            try:
                mod = importlib.import_module(collector_module)
            except:
                logger.warning('Could not load module for ' + collector_module)
                raise
        else:
            mod = sys.modules[collector_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, content.__class__.__name__)
        inst = class_(host, content, parent, args)

        return inst

    def __init__(self, host, content, parent, args=None):
        self.host = host
        self.content = content
        self.parent = parent
        self.args = args
        self.ref_mapping = {}

    def check(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def resolve_reference(self, ref):
        if ref in self.ref_mapping:
            logger.debug('Mapping reference ' + ref + ' to ' + self.ref_mapping[ref])
            ref = self.ref_mapping[ref]

        if not self.parent:
            raise RuntimeError("Got to null parent without resolving reference")

        logger.debug('Reference ' + ref + ' not in ' + self.__class__.__name__ + ' continuing to parent ' + self.parent.__class__.__name__)
        return self.parent.resolve_reference(ref)

    def set_ref_mapping(self, mapping):
        logger.debug('Updating reference mapping with ' + str(mapping))
        self.ref_mapping.update(mapping)
