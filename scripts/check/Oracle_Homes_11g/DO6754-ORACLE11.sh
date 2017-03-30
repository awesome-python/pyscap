#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME

if [[ ! -d $ORACLE_HOME/ccr ]]; then
	pass
fi

q=$(sqlplus_sysdba "select count(*) from dba_users where username = 'ORACLE_OCM';" | sed 's/^\s*//')
if [[ "$q" != 0 ]]; then
	fail "Oracle Configuration Manager is installed on a production system: user count is $q"
fi

pass
