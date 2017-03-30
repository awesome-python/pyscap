#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "SET LINESIZE 1024;
SET PAGESIZE 0;
select p1.profile profile, p1.limit REUSE_MAX, p2.limit REUSE_TIME
from dba_profiles p1, dba_profiles p2
where p1.profile = p2.profile
and p1.resource_name = 'PASSWORD_REUSE_MAX'
and p2.resource_name = 'PASSWORD_REUSE_TIME'
and ((p1.limit in ('UNLIMITED', NULL) or cast(p1.limit as integer) < 10)
or p2.limit <> 'UNLIMITED')
order by p1.profile;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Password reuse is not prevented where supported by the DBMS profiles:
$e"
fi

