#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name='audit_trail';")
if [[ "$e" =~ 'db' || "$e" =~ 'db_extended' ]]; then
	f=$(sqlplus_sysdba "select grantee from dba_tab_privs
where table_name = 'AUD\$'
and grantee not in ('DELETE_CATALOG_ROLE')
and grantee not in
(select grantee from dba_role_privs
where granted_role = 'DBA')
order by grantee;")
	fail "Audit records are not restricted to authorized individuals:
$f";
else
	pass
fi
