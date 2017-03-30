#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username from v\$pwfile_users
where username not in
(select grantee from dba_role_privs where granted_role='DBA')
and username<>'INTERNAL'
and (sysdba = 'TRUE' or sysoper='TRUE');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "The DBA role is assigned excessive or unauthorized privileges:
$e"
fi
