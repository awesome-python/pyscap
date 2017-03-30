#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee||': '||PRIVILEGE from dba_sys_privs
where privilege<>'CREATE SESSION'
and grantee not in
('ANONYMOUS',
'AQ_ADMINISTRATOR_ROLE',
'AQ_USER_ROLE',
'AURORA\$JIS\$UTILITY\$',
'AURORA\$ORB\$UNAUTHENTICATED',
'CONNECT',
'CTXSYS',
'DATAPUMP_EXP_FULL_DATABASE',
'DATAPUMP_IMP_FULL_DATABASE',
'DBA',
'DBSNMP',
'DELETE_CATALOG_ROLE',
'EXECUTE_CATALOG_ROLE',
'EXP_FULL_DATABASE',
'GATHER_SYSTEM_STATISTICS',
'HS_ADMIN_ROLE',
'IMP_FULL_DATABASE',
'JAVADEBUGPRIV',
'LOGSTDBY_ADMINISTRATOR',
'MDSYS',
'MTSSYS',
'ODM',
'ODM_MTR',
'OEM_ADVISOR',
'OEM_MONITOR',
'OLAPSYS',
'OLAP_DBA',
'OLAP_USER',
'ORDPLUGINS',
'ORDSYS',
'OSE\$HTTP\$ADMIN',
'OUTLN',
'PUBLIC',
'RECOVERY_CATALOG_OWNER',
'RESOURCE',
'RMAN',
'SCHEDULER_ADMIN',
'SELECT_CATALOG_ROLE',
'SNMPAGENT',
'SYS',
'SYSMAN',
'SYSTEM',
'TIMESERIES_DBA',
'TIMESERIES_DEVELOPER',
'WKPROXY',
'WKSYS',
'WKUSER',
'WMSYS',
'WM_ADMIN_ROLE',
'XDB')
and grantee not in
(select grantee from dba_role_privs where granted_role='DBA')
and grantee not in
(select username from dba_users where upper(account_status) like
'%LOCKED%');")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	pass
fi

fail "Oracle system privileges are directly assigned to unauthorized accounts:
$e"