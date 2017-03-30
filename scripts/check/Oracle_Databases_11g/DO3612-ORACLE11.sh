#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select privilege from dba_sys_privs where grantee = 'PUBLIC';")
if [[ "x$e" != $'x\nno rows selected' ]]; then
	fail "System Privileges are granted to PUBLIC:
$e"
fi

pass