#!/bin/bash

. lib/oracle.sh

p=$(dba_privs)
a="'SYS',
'SYSTEM',
'WMSYS'"

e=$(sqlplus_sysdba "select
	grantee grantee,
	granted_role priv
from    dba_role_privs
where   grantee in (select username from dba_users where username not in ($a))
	and granted_role in ($p)
union
select
	grantee grantee,
	privilege priv
from    dba_sys_privs
where   grantee in (select username from dba_users where username not in ($a))
	and privilege in ($p)
union
select
	grantee grantee,
	privilege priv
from    dba_tab_privs
where   grantee in (select username from dba_users where username not in ($a))
	and privilege in ($p)
union
select
	grantee grantee,
	privilege priv
from    dba_col_privs
where   grantee in (select username from dba_users where username not in ($a))
	and privilege in ($p);")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "DBMS application user roles should not be assigned unauthorized privileges:
$e"
fi
