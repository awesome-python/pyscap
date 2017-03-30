#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee, privilege from dba_sys_privs
where grantee not in
('SYS', 'SYSTEM', 'AQ_ADMINISTRATOR_ROLE', 'DBA',
'MDSYS', 'LBACSYS', 'SCHEDULER_ADMIN',
'WMSYS')
and admin_option = 'YES'
and grantee not in
(select grantee from dba_role_privs where granted_role = 'DBA');")
if [[ "x$e" != $'x\nno rows selected' ]]; then
	fail "System privileges granted using the WITH ADMIN OPTION are granted to unauthorized user accounts:
$e"
fi

pass