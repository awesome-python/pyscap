#!/bin/bash

. lib/oracle.sh

na_if_db_conf_public
na_if_db_conf_sensitive

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'audit_sys_operations';")
if [[ $e =~ 'no rows selected' ]]; then
	fail 'audit_sys_operations parameter not found'
fi

if [[ "x$e" == $'xFALSE' ]]; then
	fail "Changes to configuration options are not audited:
$e"
elif [[ "x$e" == $'xTRUE' ]]; then
	pass
else
	fail "audit_sys_operations parameter with unknown value:
$e"
fi

