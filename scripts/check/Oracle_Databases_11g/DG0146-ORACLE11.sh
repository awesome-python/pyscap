#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "SELECT privilege,SUCCESS,FAILURE from dba_priv_audit_opts;" | egrep "^CREATE SESSION\s+(BY ACCESS|NOT SET)\s+BY ACCESS\$")

if [[ "x$e" = "x" ]]; then
	fail "CREATE SESSION is not being audited"
else
	pass
fi