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
import argparse
import atexit
from io import StringIO
import logging
import pprint
import sys
import time
import xml.dom.minidom
import xml.etree.ElementTree as ET

from scap.ColorFormatter import ColorFormatter
from scap.Model import Model
from scap.model import NAMESPACES
from scap.Host import Host
from scap.Inventory import Inventory
from scap.collector.Checker import Checker
from scap.Reporter import Reporter

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
logger = logging.getLogger(__name__)
logger.debug('Start: ' + time.asctime(time.localtime()))
def end_func():
    output.close()
    logger.debug('End: ' + time.asctime(time.localtime()))
atexit.register(end_func)

# set up argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--version', action='version', version='%(prog)s 1.0')
arg_parser.add_argument('--verbose', '-v', action='count')

group = arg_parser.add_mutually_exclusive_group()
group.add_argument('--collect', help='try to connect and collect facts from the host', action='store_true')
group.add_argument('--benchmark', help='benchmark hosts', action='store_true')
group.add_argument('--list-hosts', help='outputs a list of the hosts', action='store_true')
# group.add_argument('--test', help='perform a test on the selected hosts', nargs='+')
group.add_argument('--parse', help='parse the supplied files', nargs='+', type=argparse.FileType('r'))

# pre-parse arguments
args = arg_parser.parse_known_args()
if len(args) <= 0:
    arg_parser.error('No valid operation was given')

# change verbosity
if args[0].verbose:
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
if args[0].collect:
    logger.info("Collect operation")
    arg_parser.add_argument('--inventory', nargs='+')
    arg_parser.add_argument('--host', nargs='+')
elif args[0].benchmark:
    logger.info("Benchmark operation")
    arg_parser.add_argument('--inventory', nargs='+')
    arg_parser.add_argument('--host', nargs='+')
    arg_parser.add_argument('--content', required=True, nargs='+')
    arg_parser.add_argument('--data_stream', nargs=1)
    arg_parser.add_argument('--checklist', nargs=1)
    arg_parser.add_argument('--profile', nargs=1)
    arg_parser.add_argument('--output', nargs='?', default='-')
    arg_parser.add_argument('--pretty', action='store_true')
elif args[0].list_hosts:
    arg_parser.add_argument('--host', nargs='+')
    arg_parser.add_argument('--inventory', nargs='+')
# elif args[0].test:
#     logger.info("Test operation")
#     arg_parser.add_argument('--host', required=True, nargs='+')
#     # test argument is already defined
#     arg_parser.add_argument('--object', required=True, nargs='+')
#     arg_parser.add_argument('--state', required=True, nargs='+')
else:
    arg_parser.error('No valid operation was given')

# final argument parsing
args = vars(arg_parser.parse_args())

# configure ElementTree
for k,v in list(NAMESPACES.items()):
    ET.register_namespace(v, k)

# expand the hosts
if args['collect'] or args['benchmark'] or args['list_hosts']:
    inventory = Inventory()
    for filename in args['inventory']:
        try:
            with open(filename, 'r') as fp:
                logger.debug('Loading inventory from ' + filename)
                Inventory().readfp(fp)
        except IOError:
            logger.error('Could not read from inventory file ' + filename)

    if len(args['host']) == 0:
        arg_parser.error('No host specified (--host)')

    hosts = []
    for hostname in args['host']:
        host = Host.load(hostname)
        hosts.append(host)

# open output if it's not stdout
if args['output'] != '-':
    output = open(uri, mode='w')
else:
    output = sys.stdout

if args['collect']:
    for host in hosts:
        host.connect()
        for collector in host.detect_collectors(args):
            collector.collect()
        host.disconnect()

        logger.info('Fact collection dump:')
        pp = pprint.PrettyPrinter(width=132)
        pp.pprint(host.facts)
elif args['benchmark']:
    ### Loading.Import
    # Import the XCCDF document into the program and build an initial internal
    # representation of the Benchmark object, Groups, Rules, and other objects.
    # If the file cannot be read or parsed, then Loading fails. (At the
    # beginning of this step, any inclusion processing specified with XInclude
    # elements should be performed. The resulting XML information set should be
    # validated against the XCCDF schema given in Appendix A.) Go to the next
    # step: Loading.Noticing.

    if len(args['content']) == 0:
        arg_parser.error('No content specified (--content)')

    for uri in args['content']:
        logger.debug('Loading content file: ' + uri)
        with open(uri, mode='r', encoding='utf_8') as f:
            content = Model.load(None, ET.parse(f).getroot(), uri)

    for host in hosts:
        host.connect()
        for collector in host.detect_collectors(args):
            collector.collect()
        chk = Checker.load(host, args, content)
        chk.collect()
        host.disconnect()

    rep = Reporter.load(hosts, content, args)
    report = rep.report()

    if args['pretty']:
        sio = StringIO()
        report.write(sio, encoding='unicode', xml_declaration=True)
        sio.write("\n")

        pretty_xml = xml.dom.minidom.parseString(sio.getvalue()).toprettyxml(indent='  ')
        output.write(pretty_xml)
    else:
        report.write(output, encoding='unicode')
elif args['list_hosts']:
    print('Hosts: ')
    for host in hosts:
        print(host.hostname)
elif args['test']:
    arg_parser.error('Unimplemented')
else:
    arg_parser.error('No valid operation was given')
