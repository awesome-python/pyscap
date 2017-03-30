#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee||': '||privilege
from dba_sys_privs
where grantee not in
('ANONYMOUS',
'APPQOSSYS',
'CTXSYS',
'DBSNMP',
'DIP',
'MDSYS',
'ORACLE_OCM',
'OUTLN',
'SYS',
'SYSMAN',
'SYSTEM',
'WKSYS',
'WMSYS',
'XDB')
and grantee not in
(select distinct granted_role from dba_role_privs)
and privilege <> 'UNLIMITED TABLESPACE'
order by grantee;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Administrative privileges are not assigned to database accounts via database roles.:
$e"
fi
