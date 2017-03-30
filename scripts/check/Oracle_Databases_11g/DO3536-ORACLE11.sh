#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select limit from DBA_PROFILES
where profile = 'DEFAULT'
and resource_name = 'IDLE_TIME';")
if [[ "x$e" = "xUNLIMITED" || "$e" -gt 15 ]]; then
	fail "The IDLE_TIME profile parameter is not set for Oracle profiles IAW DoD policy:
DEFAULT: $e"
fi

e=$(sqlplus_sysdba "set feed off;
select profile from DBA_PROFILES
where profile <> 'DEFAULT'
and resource_name = 'IDLE_TIME';")
for i in $e; do
	q=$(sqlplus_sysdba "select limit from DBA_PROFILES
	where profile = '$i'
	and resource_name = 'IDLE_TIME';")
	if [[ "x$q" = "xUNLIMITED" || "$q" -gt 60 ]]; then
		fail "The IDLE_TIME profile parameter is not set for Oracle profiles IAW DoD policy:
	$i: $q"
	fi
done

pass