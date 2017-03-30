#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username, tablespace_name from dba_ts_quotas
where username not in (select distinct owner from dba_objects)
and username not in (select grantee from dba_role_privs where granted_role='DBA');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
fi

fail "Database application user accounts have not been denied storage usage for object creation within the
database:
$e"