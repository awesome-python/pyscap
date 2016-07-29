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

import inspect, urlparse, logging
from scap.CredentialStore import CredentialStore

logger = logging.getLogger(__name__)
class Host(object):
    # TODO should be in a config file
    DEFAULT_SCHEME = 'ssh'

    @staticmethod
    def parse(spec):
        if spec.find('://') == -1:
            spec = Host.DEFAULT_SCHEME + '://' + spec
        url = urlparse.urlparse(spec)
        if url.scheme == 'ssh':
            creds = CredentialStore()
            if creds.has_section(url.hostname):
                if url.username:
                    creds.set(url.hostname, 'ssh_username', url.username)
                if url.password:
                    creds.set(url.hostname, 'ssh_password', url.password)
            from scap.host.SSHHost import SSHHost
            t = SSHHost(url.hostname, port=(url.port if url.port else 22))
        elif url.scheme == 'winrm':
            from scap.host.winrm_host import WinRMHost
            #t = winrm_host.WinRMHost(url.hostname, port=(url.port if url.port else 0))
            raise NotImplementedError('winrm hosts are not implemented')
        else:
            logger.critical('Unsupported host scheme: ' + url.scheme)
            sys.exit()
        return t

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.fact_collectors = []

    def get_hostname(self):
        return self.hostname

    def line_from_command(self, cmd):
        return self.exec_command(cmd).readline()

    def lines_from_command(self, cmd):
        return self.exec_command(cmd).readlines()

    def line_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readline()

    def lines_from_priv_command(self, cmd):
        return self.exec_privileged_command(cmd).readlines()

    def connect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def disconnect(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def exec_command(self, cmd):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def can_privileged_command(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
    def exec_privileged_command(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def collect_facts(self):
        self.facts = {}

        # have to use while vs. for loop so collectors can add other collectors
        i = 0
        while i < len(self.fact_collectors):
            try:
                self.fact_collectors[i].collect()
            except Exception, e:
                import traceback
                logger.warning('Fact collector ' + self.fact_collectors[i].__class__.__name__ + ' failed: ' + e.__class__.__name__ + ' ' + str(e) + ':\n' + traceback.format_exc())
            i += 1

    def benchmark(self, content, args):
        from scap.collector.ResultCollector import ResultCollector
        col = ResultCollector.load(self, content, args)
        self.results = col.collect()
