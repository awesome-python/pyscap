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
class Extendable(Model):
    MODEL_MAP = {
        # abstract
    }

    PROCESSING_MAP = {
        'abstract': 'none',
        'cluster_id': 'none',
        'extends': 'none',
        'id': 'none',
        'signature': 'none',
        'status': 'none',

        'source': 'prepend',
        'choices': 'prepend',

        'requires': 'append',
        'conflicts': 'append',
        'ident': 'append',
        'fix': 'append',
        'value': 'append',
        'default': 'append',
        'operator': 'append',
        'lower_bound': 'append',
        'upper_bound': 'append',
        'match': 'append',
        'note_tag': 'append',
        'settings': 'append',   # replaces select, set-value, set-complex-value, refine-rule, refine-value elements

        'hidden': 'replace',
        'prohibitChanges': 'replace',
        'selected': 'replace',
        'version': 'replace',
        'weight': 'replace',
        'operator': 'replace',
        'interfaceHint': 'replace',
        'check': 'replace',
        'complex_check': 'replace',
        'role': 'replace',
        'severity': 'replace',
        'type': 'replace',
        'interactive': 'replace',
        'multiple': 'replace',

        'title': 'override',
        'description': 'override',
        'platform': 'override',
        'question': 'override',
        'rationale': 'override',
        'warning': 'override',
        'reference': 'override',
        'fixtext': 'override',
        'profileNote': 'override',
    }

    def resolve_property(self, extended, property_name):
        if not hasattr(self, 'resolved_properties'):
            self.resolved_properties = []

        if property_name in self.resolved_properties:
            return

        if property_name not in self.PROCESSING_MAP:
            raise ValueError('Unable to resolve unknown property: ' + property_name)

        if not hasattr(extended, property_name):
            self.resolved_properties += property_name
            return

        extended_prop = getattr(extended, property_name)

        logger.debug('Using inheritance model ' + self.PROCESSING_MAP[property_name] + ' for ' + property_name + ' on ' + self.__class__.__name__ + ' id: ' + self.id)
        # None
        # These properties cannot be inherited at all; they must be given explicitly
        if self.PROCESSING_MAP[property_name] == 'none':
            pass

        # Prepend
        elif self.PROCESSING_MAP[property_name] == 'prepend':
            if not hasattr(self, property_name):
                if isinstance(extended_prop, list) or isinstance(extended_prop, dict):
                    setattr(self, property_name, extended_prop.copy())
                else:
                    setattr(self, property_name, extended_prop)
            else:
                self_prop = getattr(self, property_name)
                if isinstance(extended_prop, list):
                    extended_prop = extended_prop.copy()
                    extended_prop.extend(self_prop)
                    setattr(self, property_name, extended_prop)
                elif isinstance(extended_prop, dict):
                    extended_prop = extended_prop.copy()
                    self_prop.update(extended_prop)
                else:
                    setattr(self, property_name, extended_prop)

        # Append
        # Additional rules may apply during Benchmark processing, tailoring, or report generation
        elif self.PROCESSING_MAP[property_name] == 'append':
            if not hasattr(self, property_name):
                if isinstance(extended_prop, list) or isinstance(extended_prop, dict):
                    setattr(self, property_name, extended_prop.copy())
                else:
                    setattr(self, property_name, extended_prop)
            else:
                self_prop = getattr(self, property_name)
                if isinstance(extended_prop, list):
                    self_prop.extend(extended_prop.copy())
                elif isinstance(extended_prop, dict):
                    extended_prop = extended_prop.copy()
                    extended_prop.update(self_prop)
                    setattr(self, property_name, extended_prop)
                else:
                    setattr(self, property_name, extended_prop)

        # Replace
        # For the check property, checks from different systems are considered different properties
        elif self.PROCESSING_MAP[property_name] == 'replace':
            if isinstance(extended_prop, list) or isinstance(extended_prop, dict):
                setattr(self, property_name, extended_prop.copy())
            else:
                setattr(self, property_name, extended_prop)

        # Override
        # For properties that have a locale (xml:lang specified), values with different locales are considered to be different properties
        elif self.PROCESSING_MAP[property_name] == 'override':
            # TODO, just replacing for now
            if isinstance(extended_prop, list) or isinstance(extended_prop, dict):
                setattr(self, property_name, extended_prop.copy())
            else:
                setattr(self, property_name, extended_prop)

        else:
            raise ValueError('Unable to resolve property: ' + property_name + ' unknown processing model: ' + self.PROCESSING_MAP[property_name])

        self.resolved_properties += property_name

    def get_extended(self, benchmark):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def resolve(self, benchmark):
        if self.resolved:
            logger.debug('Extendable already resolved: ' + self.id)
            return
        ### Loading.Resolve.Items

        # For each Item in the Benchmark that has an extends property, resolve
        # it by using the following steps:
        if self.extends is None:
            logger.debug('Extendable not extending: ' + self.id)
            return

        # (2) resolve the extended Item,
        extended = self.get_extended(benchmark)
        logger.debug('Found extended Extendable: ' + extended.id)
        extended.resolve(benchmark)

        # (3) prepend the property sequence from the extended Item to the
        # extending Item,
        # (5) remove duplicate properties and apply property overrides, and
        for name in self.model_map['attributes']:
            attr_map = self.model_map['attributes'][name]
            if 'ignore' in attr_map and attr_map['ignore']:
                continue

            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xml_namespace, attr_name = Model.parse_tag(name)
                attr_name = attr_name.replace('-', '_')
            self.resolve_property(extended, attr_name)

        for tag in self.model_map['elements']:
            xml_namespace, tag_name = Model.parse_tag(tag)
            if tag.endswith('*'):
                continue

            tag_map = self.model_map['elements'][tag]
            if 'ignore' in tag_map and tag_map['ignore']:
                continue

            if 'append' in tag_map:
                self.resolve_property(extended, tag_map['append'])
            elif 'map' in tag_map:
                self.resolve_property(extended, tag_map['map'])
            else:
                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = tag_name.replace('-', '_')
            self.resolve_property(extended, name)

        # (6) remove the extends property.
        self.extends = None

        # If the directed graph formed by the extends properties includes a
        # loop, then Loading fails.
        # TODO

        # Otherwise, go to the next step: Loading.Resolve.Profiles.
