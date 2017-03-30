#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee||': '||granted_role from dba_role_privs
where grantee not in
('DBA',
'SYS',
'SYSTEM',
'WKSYS',
'LBACSYS',
'WMSYS',
'OWBSYS',
'CTXSYS',
'SPATIAL_CSW_ADMIN_USR',
'SPATIAL_WFS_ADMIN_USR',
'FLOWS_030000')
and admin_option = 'YES'
and grantee not in
(select distinct owner from dba_objects)
and grantee not in
(select grantee from dba_role_privs
where granted_role = 'DBA')
order by grantee;")
if [[ "x$e" != $'x\nno rows selected' ]]; then
	fail "Oracle roles granted using the WITH ADMIN OPTION are granted to unauthorized accounts:
$e"
fi

pass