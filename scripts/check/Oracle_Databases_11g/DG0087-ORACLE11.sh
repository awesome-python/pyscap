#!/bin/bash

. lib/oracle.sh

fail_if_ols_not_installed

e=$(sqlplus_sysdba "select * from DBA_SA_USERS;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Sensitive data should be labeled:
$e"
fi
