#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select profile, limit
from dba_profiles
where resource_name='PASSWORD_VERIFY_FUNCTION' and limit = 'NULL';")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "DBMS login accounts require passwords to meet complexity requirements:
$e"
fi
