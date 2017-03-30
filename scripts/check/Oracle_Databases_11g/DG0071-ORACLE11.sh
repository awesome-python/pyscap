#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select profile, limit from dba_profiles
where resource_name='PASSWORD_VERIFY_FUNCTION'
and limit not in ('NULL', 'DEFAULT')
order by profile;")
if [[ "x$e" != $'x\nno rows selected' ]]; then
	pass
else
	fail "No password verify function found"
fi
