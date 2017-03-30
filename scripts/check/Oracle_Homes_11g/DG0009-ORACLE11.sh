#!/bin/bash

. lib/oracle.sh
. lib/general.sh

q=`su -l oracle -c umask`
if umask_gt $q '0022'; then
	fail "Access to DBMS software files and directories are granted to unauthorized users: $q <= 0022"
else
	pass
fi
