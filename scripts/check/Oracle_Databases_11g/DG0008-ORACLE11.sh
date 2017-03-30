#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select distinct owner from dba_objects
where owner not in 
('ANONYMOUS',
'APPQOSSYS',
'AURORA\$JIS\$UTILITY\$',
'AURORA\$ORB\$UNAUTHENTICATED',
'CTXSYS',
'DBSNMP',
'DIP',
'DVF',
'DVSYS',
'EXFSYS',
'LBACSYS',
'MDDATA',
'MDSYS',
'MGMT_VIEW',
'ODM',
'ODM_MTR',
'OLAPSYS',
'ORACLE_OCM',
'ORDPLUGINS',
'ORDSYS',
'OSE\$HTTP\$ADMIN',
'OUTLN',
'PERFSTAT',
'PUBLIC',
'REPADMIN',
'RMAN',
'SI_INFORMTN_SCHEMA',
'SYS',
'SYSMAN',
'SYSTEM',
'TRACESVR',
'TSMSYS',
'WKPROXY',
'WKSYS',
'WKUSER',
'WK_TEST',
'WMSYS',
'XDB')
and owner not in
(select grantee from dba_role_privs where granted_role='DBA');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Non-Oracle object owners:
$e";
fi