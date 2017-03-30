#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select account_status from dba_users
where upper(username) = 'DBSNMP';")
if [[ "$q" = $'\nno rows returned' ]]; then
	pass
fi

fail "The Oracle Management Agent is installed, not required, not authorized or on a database accessible from the
Internet: DBSNMP account_status is $q"