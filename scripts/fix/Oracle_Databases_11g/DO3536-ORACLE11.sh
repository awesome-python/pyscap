#!/bin/bash

. lib/oracle.sh

sqlplus_sysdba "alter profile default limit idle_time 15;"

e=$(sqlplus_sysdba "set feed off;
select profile from DBA_PROFILES
where profile <> 'DEFAULT'
and resource_name = 'IDLE_TIME';")
for i in $e; do
	q=$(sqlplus_sysdba "select limit from DBA_PROFILES
	where profile = '$i'
	and resource_name = 'IDLE_TIME';")
	if [[ "x$q" = "xUNLIMITED" || "$q" -gt 60 ]]; then
		sqlplus_sysdba "alter profile $i limit idle_time 15;"
	fi
done

