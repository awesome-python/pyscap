#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee||': '||privilege||': '||owner||'.'||table_name
from dba_tab_privs where grantee not in
(select role from dba_roles)
and grantee not in
('APEX_PUBLIC_USER',
'APPQOSSYS',
'AURORA\$JIS\$UTILITY\$',
'CTXSYS',
'DBSNMP',
'EXFSYS',
'FLOWS_030000',
'FLOWS_FILES',
'LBACSYS',
'MDSYS',
'MGMT_VIEW',
'ODM',
'OLAPSYS',
'ORACLE_OCM',
'ORDPLUGINS',
'ORDSYS',
'OSE\$HTTP\$ADMIN',
'OUTLN',
'OWBSYS',
'PERFSTAT',
'PUBLIC',
'REPADMIN',
'SYS',
'SYSMAN',
'SYSTEM',
'WKSYS',
'WMSYS',
'XDB')
and table_name<>'DBMS_REPCAT_INTERNAL_PACKAGE'
and table_name not like '%RP'
and grantee not in
(select grantee from dba_tab_privs
where table_name in ('DBMS_DEFER', 'DEFLOB'));")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Application users privileges have not been restricted to assignment using application user roles:
$e"
fi
