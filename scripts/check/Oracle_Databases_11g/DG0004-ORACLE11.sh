#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select distinct owner from dba_objects, dba_users
where owner not in 
('ANONYMOUS',
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
'WK_TEST',
'WKPROXY',
'WKSYS',
'WKUSER',
'WMSYS',
'XDB')
and owner in (select distinct owner from dba_objects where object_type <> 'SYNONYM')
and owner = username
and upper(account_status) not like '%LOCKED%';")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Accounts not locked:
$e";
fi