#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee||': '||granted_role from dba_role_privs
where grantee not in 
('ANONYMOUS',
'AURORA\$JIS\$UTILITY\$',
'AURORA\$ORB\$UNAUTHENTICATED',
'CTXSYS',
'DBSNMP',
'DIP',
'DMSYS',
'DVF',
'DVSYS',
'EXFSYS',
'LBACSYS',
'MDDATA',
'MDSYS',
'MGMT_VIEW',
'ODM',
'ODM_MTR',
'OEM_MONITOR',
'OLAPSYS',
'ORDPLUGINS',
'ORDSYS',
'OSE\$HTTP\$ADMIN',
'OUTLN',
'PERFSTAT',
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
and grantee not in
('DBA',
'OLAP_USER',
'IP',
'ORASSO_PUBLIC',
'PORTAL_PUBLIC',
'DATAPUMP_EXP_FULL_DATABASE',
'DATAPUMP_IMP_FULL_DATABASE',
'EXP_FULL_DATABASE',
'IMP_FULL_DATABASE',
'OLAP_DBA',
'EXECUTE_CATALOG_ROLE',
'SELECT_CATALOG_ROLE',
'JAVASYSPRIV')
and grantee not in
(select grantee from dba_role_privs where granted_role = 'DBA')
and grantee not in (select distinct owner from dba_objects)
and granted_role in
('AQ_ADMINISTRATOR_ROLE',
'AQ_USER_ROLE',
'CTXAPP',
'DELETE_CATALOG_ROLE',
'EJBCLIENT',
'EXECUTE_CATALOG_ROLE',
'EXP_FULL_DATABASE',
'GATHER_SYSTEM_STATISTICS',
'GLOBAL_AQ_USER_ROLE',
'HS_ADMIN_ROLE',
'IMP_FULL_DATABASE',
'JAVADEBUGPRIV',
'JAVAIDPRIV',
'JAVASYSPRIV',
'JAVAUSERPRIV',
'JAVA_ADMIN',
'JAVA_DEPLOY',
'LOGSTDBY_ADMINISTRATOR',
'OEM_MONITOR',
'OLAP_DBA',
'RECOVERY_CATALOG_OWNER',
'SALES_HISTORY_ROLE',
'SELECT_CATALOG_ROLE',
'WKUSER',
'WM_ADMIN_ROLE',
'XDBADMIN')
and granted_role not in 
('CONNECT',
'RESOURCE',
'AUTHENTICATEDUSER')
order by grantee;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Database privileged role assignments should be restricted to IAO-authorized DBMS accounts:
$e"
fi
