#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'audit_trail';")
if [[ "x$e" =~ "NONE" ]]; then
	fail "Required auditing parameters for database auditing not set:
$e";
else
	pass
fi
