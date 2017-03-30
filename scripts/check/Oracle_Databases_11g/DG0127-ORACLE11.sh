#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "SET LINESIZE 1024;
SET PAGESIZE 0;
select distinct limit from dba_profiles
where resource_name= 'PASSWORD_VERIFY_FUNCTION'
and limit <> 'VERIFY_PASSWORD_DOD'
order by limit;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "DBMS account passwords are set to easily guessed words or values:
$e"
fi

