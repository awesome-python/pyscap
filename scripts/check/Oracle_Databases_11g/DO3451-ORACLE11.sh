#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee||': '||owner||'.'||table_name from dba_tab_privs
where grantable = 'YES'
and owner not in (select distinct owner from dba_objects)
and grantee not in
(select grantee from dba_role_privs where granted_role = 'DBA')
order by grantee;")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	pass
fi

fail "The Oracle WITH GRANT OPTION privilege has been granted to non-DBA or non-Application administrator
user accounts:
$e"