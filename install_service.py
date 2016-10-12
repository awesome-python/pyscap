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

from smb.SMBConnection import SMBConnection
from nmb.NetBIOS import NetBIOS
import socket
import sys
import getpass
import random
import string

if len(sys.argv) <= 1:
    sys.exit('Usage: ' + sys.argv[0] + ' target')

target = sys.argv[1]

# figure out if the given target is an IP or a nb name
target_ip = None
target_nb_name = None
try:
    socket.inet_aton(target)
    print('Target is an IP address')
    target_ip = target
except OSError as e:
    print('Target is not an IP address, trying DNS resolution')
    try:
        target_ip = socket.gethostbyname(target)
        print('Target is DNS resolvable')
    except socket.gaierror as e:
        print('Target is not DNS resolvable, assuming NB name')
        target_nb_name = target

nb = NetBIOS()

if target_ip is None:
    print('Looking up IP from target NetBIOS name ' + target_nb_name)
    ips = nb.queryName(target_nb_name)
    print('Got IPs:' + str(ips))
    if ips is None or len(ips) < 1:
        raise RuntimeError('Cannot connect to host ' + target + '; looking up NetBIOS IP failed')
    target_ip = ips[0]

if target_nb_name is None:
    print('Looking up NetBIOS name from target IP: ' + target_ip)
    nb_names = nb.queryIPForName(target_ip)
    print('Got NB names: ' + str(nb_names))
    if nb_names is None or len(nb_names) < 1:
        raise RuntimeError('Cannot connect to host ' + target + '; looking up NetBIOS name failed')
    target_nb_name = nb_names[0]

nb.close()

client_machine_name = socket.gethostbyaddr(socket.gethostname())[0]
# client_machine_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
# print('Generated client machine name: ' + client_machine_name + '\n')

domain = input('Enter domain [none]: ')
username = input('Enter username: ')
password = getpass.getpass('Enter password: ')

conn = SMBConnection(username, password, client_machine_name, target_nb_name, domain=domain,
    use_ntlm_v2 = True, sign_options=SMBConnection.SIGN_WHEN_SUPPORTED)
if not conn.connect(target_ip):
    raise RuntimeError('Could not connect to host ' + target + '; establishing connection failed')

if conn.echo('blah') != 'blah':
    raise RuntimeError('Connection test (echo) failed')

conn.close()
