#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select count(*) from dba_users where username like 'FLOWS_%';" | sed 's/^\s*//')
if [[ "$q" != 0 ]]; then
	fail "Oracle Application Express or Oracle HTML DB is installed on a production database: user count is $q"
fi

pass
