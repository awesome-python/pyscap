#!/bin/bash

. lib/oracle.sh

f=$ORACLE_HOME/network/admin/listener.ora
if [[ ! -f $f ]]; then
	fail "Passwords are not encrypted when transmitted across the network: no listener.ora"
fi

# TODO can't find out how to turn OFF password encryption, it's on by default

pass