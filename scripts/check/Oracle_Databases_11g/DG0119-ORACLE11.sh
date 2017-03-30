#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee, owner, table_name, privilege from dba_tab_privs
where privilege in ('ALTER', 'REFERENCES', 'INDEX')
and grantee not in 
('DBA',
'LBACSYS',
'SYS',
'SYSTEM',
'XDBADMIN')
and table_name not in
('SDO_IDX_TAB_SEQUENCE', 'XDB$ACL', 'XDB_ADMIN')
and grantee not in
(select grantee from dba_role_privs where granted_role = 'DBA')
and grantee not in (select distinct owner from dba_objects);")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "DBMS application users are granted administrative privileges to the DBMS:
$e"
fi
