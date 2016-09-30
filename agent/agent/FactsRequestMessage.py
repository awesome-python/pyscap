#!/usr/bin/env python

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
import socket
import sys
import os

from agent.Message import Message
from agent.FactsResponseMessage import FactsResponseMessage

logger = logging.getLogger(__name__)
class FactsRequestMessage(Message):
    def __init__(self, payload = None):
        if payload is not None:
            raise RuntimeError('Trying to instantiate FactsRequestMessage with non-null payload')
        super().__init__(payload)

    def respond_via(self, sock):
        facts = {
            'os.name': os.name,
            'os.getpid': os.getpid(),
            'os.supports_bytes_environ': os.supports_bytes_environ,
            'os.getcwd': os.getcwd(),
            'os.cpu_count': os.cpu_count(),
            'os.sep': os.sep,
            'os.altsep': os.altsep,
            'os.extsep': os.extsep,
            'os.pathsep': os.pathsep,
            'os.defpath': os.defpath,
            'os.linesep': os.linesep,
            'os.devnull': os.devnull,

            'socket.gethostname': socket.gethostname(),
            'socket.gethostbyaddr': socket.gethostbyaddr(socket.gethostname()),
            'socket.has_ipv6': socket.has_ipv6,

            'sys.argv': sys.argv,
            'sys.base_exec_prefix': sys.base_exec_prefix,
            'sys.base_prefix': sys.base_prefix,
            'sys.byteorder': sys.byteorder,
            'sys.builtin_module_names': sys.builtin_module_names,
            'sys.exec_prefix': sys.exec_prefix,
            'sys.executable': sys.executable,
            'sys.flags': {
                'debug': sys.flags.debug,
                'inspect': sys.flags.inspect,
                'interactive': sys.flags.interactive,
                'optimize': sys.flags.optimize,
                'dont_write_bytecode': sys.flags.dont_write_bytecode,
                'no_user_site': sys.flags.no_user_site,
                'no_site': sys.flags.no_site,
                'ignore_environment': sys.flags.ignore_environment,
                'verbose': sys.flags.verbose,
                'bytes_warning': sys.flags.bytes_warning,
                'quiet': sys.flags.quiet,
                'hash_randomization': sys.flags.hash_randomization,
            },
            'sys.float_info': {
                'epsilon': sys.float_info.epsilon,
                'dig': sys.float_info.dig,
                'mant_dig': sys.float_info.mant_dig,
                'max': sys.float_info.max,
                'max_exp': sys.float_info.max_exp,
                'max_10_exp': sys.float_info.max_10_exp,
                'min': sys.float_info.min,
                'min_exp': sys.float_info.min_exp,
                'min_10_exp': sys.float_info.min_10_exp,
                'radix': sys.float_info.radix,
                'rounds': sys.float_info.rounds,
            },
            'sys.getallocatedblocks': sys.getallocatedblocks(),
            'sys.getdefaultencoding': sys.getdefaultencoding(),
            'sys.getfilesystemencoding': sys.getfilesystemencoding(),
            'sys.hash_info': {
                'width': sys.hash_info.width,
                'modulus': sys.hash_info.modulus,
                'inf': sys.hash_info.inf,
                'nan': sys.hash_info.nan,
                'imag': sys.hash_info.imag,
                'algorithm': sys.hash_info.algorithm,
                'hash_bits': sys.hash_info.hash_bits,
                'seed_bits': sys.hash_info.seed_bits,
            },
            'sys.hexversion': sys.hexversion,
            #'sys.long_info': sys.long_info, # deprecated in 3
            'sys.implementation': {
                'name': sys.implementation.name,
                'version': {
                    'major': sys.implementation.version.major,
                    'minor': sys.implementation.version.minor,
                    'micro': sys.implementation.version.micro,
                    'releaselevel': sys.implementation.version.releaselevel,
                    'serial': sys.implementation.version.serial,
                },
                'hexversion': sys.implementation.hexversion,
                'cache_tag': sys.implementation.cache_tag,
            },
            'sys.int_info': {
                'bits_per_digit': sys.int_info.bits_per_digit,
                'sizeof_digit': sys.int_info.sizeof_digit,
            },
            #'sys.maxint': sys.maxint, # deprecated in 3
            'sys.maxsize': sys.maxsize,
            'sys.maxunicode': sys.maxunicode,
            'sys.modules': list(sys.modules.keys()),
            'sys.path': sys.path,
            'sys.platform': sys.platform,
            'sys.prefix': sys.prefix,
            'sys.thread_info': {
                'name': sys.thread_info.name,
                'lock': sys.thread_info.lock,
                'version': sys.thread_info.version,
            },
            'sys.version': sys.version,
            'sys.api_version': sys.api_version,
            'sys.version_info': {
                'major': sys.version_info.major,
                'minor': sys.version_info.minor,
                'micro': sys.version_info.micro,
                'releaselevel': sys.version_info.releaselevel,
                'serial': sys.version_info.serial,
            },
        }

        facts['os.environ'] = {k: v for (k,v) in os.environ.items()}

        # Availability: Windows
        if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
            facts['os.getlogin'] = os.getlogin()
            facts['os.getpid'] = os.getpid()
            facts['os.getppid'] = os.getppid()

            winver = sys.getwindowsversion()
            facts['sys.getwindowsversion'] = {
                'major': winver.major,
                'minor': winver.minor,
                'build': winver.build,
                'platform': winver.platform,
                'service_pack': winver.service_pack,
                'service_pack_minor': winver.service_pack_minor,
                'service_pack_major': winver.service_pack_major,
                'suite_mask': winver.suite_mask,
                'product_type': winver.product_type,
            }
            facts['sys.dllhandle'] = sys.dllhandle

        # # Availability: Unix/POSIX
        # # we're assuming Unix == POSIX for this purpose
        # if sys.platform.startswith('linux') or sys.platform.startswith('freebsd') or sys.platform.startswith('darwin'):
        #     facts['sys.abiflags'] = sys.abiflags
        #     facts['os.getegid'] = os.getegid()
        #     facts['os.geteuid'] = os.geteuid()
        #     facts['os.getgid'] = os.getgid()
        #     facts['os.getgroups'] = os.getgroups()
        #     facts['os.getlogin'] = os.getlogin()
        #     facts['os.getpgid'] = os.getpgid()
        #     facts['os.getpgrp'] = os.getpgrp()
        #     facts['os.getpid'] = os.getpid()
        #     facts['os.getppid'] = os.getppid()
        #     facts['os.getpriority'] = os.getpriority()
        #     facts['os.getresuid'] = os.getresuid()
        #     facts['os.getresgid'] = os.getresgid()
        #     facts['os.getuid'] = os.getuid()
        #     facts['os.getloadavg'] = os.getloadavg()
        #     facts['os.uname'] = os.uname()
        #
        #     facts['socket.if_nameindex'] = socket.if_nameindex()
        #     facts['sys.getdlopenflags'] = sys.getdlopenflags()

        resp = FactsResponseMessage(facts)
        resp.send_via(sock)
