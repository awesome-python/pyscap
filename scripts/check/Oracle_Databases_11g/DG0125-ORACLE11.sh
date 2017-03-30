#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "SET LINESIZE 1024;
SET PAGESIZE 0;
select profile, LIMIT
from dba_profiles
where (resource_name='PASSWORD_LIFE_TIME') AND (\"LIMIT\" in ('UNLIMITED', NULL) OR (cast (LIMIT as integer) > 60));")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "DBMS account passwords are not set to expire every 60 days or more frequently in profiles:
$e"
fi

