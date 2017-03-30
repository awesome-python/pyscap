#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "SET LINESIZE 1024;
SET PAGESIZE 0;
select profile, limit from dba_profiles
where resource_name = 'PASSWORD_LOCK_TIME'
and limit not in ('UNLIMITED', 'DEFAULT');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Unlimited account lock times are not specified for locked accounts:
$e"
fi

