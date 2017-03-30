#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee, privilege from dba_sys_privs
where (privilege like 'CREATE%' or privilege like 'ALTER%'
or privilege like 'DROP%')
and privilege<>'CREATE SESSION'
and grantee not in
('ANONYMOUS',
'APPQOSSYS',
'AQ_ADMINISTRATOR_ROLE',
'AURORA\$JIS\$UTILITY\$',
'AURORA\$ORB\$UNAUTHENTICATED',
'CTXSYS',
'DATAPUMP_EXP_FULL_DATABASE',
'DATAPUMP_IMP_FULL_DATABASE',
'DBA',
'DBSNMP',
'DIP',
'DVF',
'DVSYS',
'EXFSYS',
'EXP_FULL_DATABASE',
'IMP_FULL_DATABASE',
'LBACSYS',
'MDDATA',
'MDSYS',
'MGMT_VIEW',
'ODM',
'ODM_MTR',
'OEM_ADVISOR',
'OEM_MONITOR',
'OLAPSYS',
'ORACLE_OCM',
'ORDPLUGINS',
'ORDSYS',
'OSE\$HTTP\$ADMIN',
'OUTLN',
'PERFSTAT',
'PUBLIC',
'RECOVERY_CATALOG_OWNER',
'REPADMIN',
'RESOURCE',
'RMAN',
'SCHEDULER_ADMIN',
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
order by grantee;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Production databases should be protected from unauthorized access by developers on shared
production/development host systems; accounts are listed that are not on the list of IAO approved production DBAs:
$e"
fi
