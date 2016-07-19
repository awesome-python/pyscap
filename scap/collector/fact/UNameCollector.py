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

from scap.collector.FactCollector import FactCollector

class UNameCollector(FactCollector):
    def collect_facts(self):
        uname = self.host.line_from_command('uname -a')
        self.host.facts['uname'] = uname
        if uname.startswith('Linux'):
            from scap.collector.fact.LinuxCollector import LinuxCollector
            self.host.add_fact_collector(LinuxCollector(self.host))
        elif uname.startswith('Darwin'):
            from scap.collector.fact.AppleCollector import AppleCollector
            self.host.add_fact_collector(AppleCollector(self.host))
        elif uname.startswith('Windows NT'):
            from scap.collector.fact.MicrosoftCollector import MicrosoftCollector
            self.host.add_fact_collector(MicrosoftCollector(self.host))
        else:
            raise NotImplementedError('Host discovery has not been implemented for uname: ' + uname)
