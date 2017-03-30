#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select granted_role from dba_role_privs where grantee = 'PUBLIC';")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	pass
fi

fail "Application role permissions are assigned to the Oracle PUBLIC role:
$e"