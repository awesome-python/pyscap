#!/bin/bash

. lib/oracle.sh

# Remote administration is not disabled for the Oracle connection manager

f=$ORACLE_HOME/network/admin/cman.ora
if [[ ! -f $f ]]; then
	notapplicable
fi

r=$(grep 'REMOTE_ADMIN\s*=\s*NO' $f)
if [[ "x$r" = "x" ]]; then
	fail "Remote administration is not disabled for the Oracle connection manager: $r"
fi

pass
