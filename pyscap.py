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

# set up logging
import logging
from scap.ColorFormatter import ColorFormatter
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename="pyscap.log", mode='w')
fh_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(fh_formatter)
ch_formatter = ColorFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(ch_formatter)
rootLogger.addHandler(ch)
rootLogger.addHandler(fh)

# report start time & end time
import time, atexit
logger = logging.getLogger(__name__)
logger.debug('Start: ' + time.asctime(time.localtime()))
def end_func():
    logger.debug('End: ' + time.asctime(time.localtime()))
atexit.register(end_func)

# set up argument parsing
import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--version', action='version', version='%(prog)s 1.0')
arg_parser.add_argument('--verbose', '-v', action='count')

group = arg_parser.add_mutually_exclusive_group()
group.add_argument('--connect', help='try to connect to the host', action='store_true')
group.add_argument('--benchmark', help='benchmark hosts', action='store_true')
group.add_argument('--list-hosts', help='outputs a list of the hosts', action='store_true')
# group.add_argument('--test', help='perform a test on the selected hosts', nargs='+')
group.add_argument('--parse', help='parse the supplied files', nargs='+', type=argparse.FileType('r'))

# pre-parse arguments
args = arg_parser.parse_known_args()

# change verbosity
if(args[0].verbose == 1):
    ch.setLevel(logging.INFO)
    logger.debug('Set console logging level to INFO')
elif(args[0].verbose == 2):
    ch.setLevel(logging.DEBUG)
    logger.debug('Set console logging level to DEBUG')
elif(args[0].verbose >= 3):
    ch.setLevel(logging.NOTSET)
    logger.debug('Set console logging level to NOTSET')

# set up the modes
if args[0].connect:
    logger.info("Connect operation")
    arg_parser.add_argument('--inventory', nargs='+')
    arg_parser.add_argument('--host', nargs='+')
elif args[0].benchmark:
    logger.info("Benchmark operation")
    arg_parser.add_argument('--inventory', nargs='+')
    arg_parser.add_argument('--host', nargs='+')
    arg_parser.add_argument('--content', required=True, nargs=1, type=argparse.FileType('r'))
    arg_parser.add_argument('--data_stream', nargs=1)
    arg_parser.add_argument('--checklist', nargs=1)
    arg_parser.add_argument('--profile', nargs=1)
    arg_parser.add_argument('--output', type=argparse.FileType('wb', 0), default='-')
    arg_parser.add_argument('--pretty', action='store_true')
elif args[0].list_hosts:
    arg_parser.add_argument('--host', nargs='+')
# elif args[0].test:
#     logger.info("Test operation")
#     arg_parser.add_argument('--host', required=True, nargs='+')
#     # test argument is already defined
#     arg_parser.add_argument('--object', required=True, nargs='+')
#     arg_parser.add_argument('--state', required=True, nargs='+')
else:
    import sys
    sys.exit('No valid operation was given')

# final argument parsing
args = arg_parser.parse_args()

# configure ElementTree
from scap.Model import Model
import xml.etree.ElementTree as ET
from scap.model import NAMESPACES
for k,v in list(NAMESPACES.items()):
    ET.register_namespace(v, k)

# perform the operations
from scap.Host import Host
from scap.Inventory import Inventory

if args.connect or args.benchmark or args.list_hosts:
    if args.inventory:
        for filename in args.inventory:
            try:
                with open(filename, 'r') as fp:
                    logger.debug('Loading inventory from ' + filename)
                    Inventory().readfp(fp)
            except IOError:
                logger.error('Could not read from inventory file ' + filename)
    if not args.host:
        logger.critical('--host <host> must be supplied')
        import sys
        sys.exit()
    hosts = []
    inventory = Inventory()
    if args.host:
        for hostname in args.host:
            if not inventory.has_section(hostname):
                logger.critical('Host not found in inventory file: ' + hostname)
                sys.exit()
            if not inventory.has_option(hostname, 'connection'):
                connection = 'ssh'
                #TODO do some kind of auto detection
            else:
                connection = inventory.get(hostname, 'connection')
            if connection == 'ssh':
                from scap.host.SSHHost import SSHHost
                host = SSHHost(hostname)
            elif connection == 'impacket':
                from scap.host.IMPacketHost import IMPacketHost
                host = IMPacketHost(hostname)
            elif connection == 'smb':
                from scap.host.SMBHost import SMBHost
                host = SMBHost(hostname)
            elif connection == 'winrm':
                from scap.host.WinRMHost import WinRMHost
                host = WinRMHost(hostname)
            else:
                logger.critical('Unsupported host connection type: ' + connection)
                sys.exit()
            hosts.append(host)

if args.connect:
    for host in hosts:
        host.connect()
        host.collect_facts()
        print(str(host.facts))
        host.disconnect()
elif args.benchmark:

    content = Model.load(None, ET.parse(args.content[0]).getroot())

    # convert args to hash for use by checkers
    checker_args = {}
    if args.data_stream:
        checker_args['data_stream'] = args.data_stream[0]
    if args.checklist:
        checker_args['checklist'] = args.checklist[0]
    if args.profile:
        checker_args['profile'] = args.profile[0]

    for host in hosts:
        host.connect()
        host.collect_facts()
        #TODO cache facts
        host.benchmark(content, checker_args)
        host.disconnect()

    from scap.Reporter import Reporter
    report = Reporter(content, hosts).report()

    if args.pretty:
        import xml.dom.minidom
        pretty_xml = xml.dom.minidom.parseString(report).toprettyxml(indent='  ')
        args.output.write(pretty_xml)
    else:
        args.output.write(report)
elif args.list_hosts:
    print('Hosts: ')
    for t in Target.parse(args):
        t.pretty()
elif args.test:
    import sys
    sys.exit('Unimplemented')
else:
    import sys
    sys.exit('No valid operation was given')
