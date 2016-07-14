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

import logging, argparse, sys, time, atexit
from StringIO import StringIO
import xml.etree.ElementTree as ET
from scap.colorformatter import ColorFormatter
from scap.engine.engine import Engine
from scap.target.target import Target
from scap.credential_store import CredentialStore

# set up logging
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

logger = logging.getLogger(__name__)
logger.debug('Start: ' + time.asctime(time.localtime()))
def end_func():
    logger.debug('End: ' + time.asctime(time.localtime()))
atexit.register(end_func)

# set up argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--version', action='version', version='%(prog)s 1.0')
arg_parser.add_argument('--verbose', '-v', action='count')

group = arg_parser.add_mutually_exclusive_group()
group.add_argument('--benchmark', help='benchmark targets', action='store_true')
group.add_argument('--list-hosts', help='outputs a list of the hosts that would be targeted', action='store_true')
# group.add_argument('--test', help='perform a test on the selected targets', nargs='+')
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
if args[0].benchmark:
    logger.info("Benchmark operation")
    arg_parser.add_argument('--credentials', nargs='+')
    arg_parser.add_argument('--target', nargs='+')
    arg_parser.add_argument('--targets', nargs='+')
    arg_parser.add_argument('--content', required=True, nargs=1, type=argparse.FileType('r'))
    arg_parser.add_argument('--data_stream', nargs=1)
    arg_parser.add_argument('--checklist', nargs=1)
    arg_parser.add_argument('--profile', nargs=1)
    arg_parser.add_argument('--output', type=argparse.FileType('wb', 0), default='-')
    arg_parser.add_argument('--pretty', action='store_true')
elif args[0].list_hosts:
    arg_parser.add_argument('--target', required=True, nargs='+')
# elif args[0].test:
#     logger.info("Test operation")
#     arg_parser.add_argument('--target', required=True, nargs='+')
#     # test argument is already defined
#     arg_parser.add_argument('--object', required=True, nargs='+')
#     arg_parser.add_argument('--state', required=True, nargs='+')
else:
    sys.exit('No valid operation was given')

# final argument parsing
args = arg_parser.parse_args()

# configure ElementTree
for prefix in Engine.namespaces:
    ET.register_namespace(prefix, Engine.namespaces[prefix])

# perform the operations
if args.benchmark:
    if args.credentials:
        for filename in args.credentials:
            try:
                with open(filename, 'r') as fp:
                    logger.debug('Loading credentials from ' + filename)
                    CredentialStore().readfp(fp)
            except IOError:
                logger.error('Could not read from file ' + filename)
    if not args.target and not args.targets:
        logger.critical('Either --target <host> or --targets <file> must be supplied')
        sys.exit()
    targets = []
    if args.target:
        for t in args.target:
            targets.append(Target.parse(t))
    if args.targets:
        for filename in args.targets:
            with open(filename, 'r') as f:
                for line in f:
                    targets.append(Target.parse(line))

    content = ET.parse(args.content[0])
    b_args = {}
    if args.data_stream:
        b_args['data_stream'] = args.data_stream[0]
        if args.checklist:
            b_args['checklist'] = args.checklist[0]
    if args.profile:
        b_args['profile'] = args.profile[0]
    engine = Engine.get_engine(content, b_args)
    engine.collect(targets)
    report = engine.report()
    if args.pretty:
        import xml.dom.minidom
        pretty_xml = xml.dom.minidom.parseString(report).toprettyxml()
        args.output.write(pretty_xml)
    else:
        args.output.write(report)
elif args.list_hosts:
    print 'Hosts: '
    for t in Target.parse(args):
        t.pretty()
elif args.test:
    sys.exit('Unimplemented')
else:
    sys.exit('No valid operation was given')
