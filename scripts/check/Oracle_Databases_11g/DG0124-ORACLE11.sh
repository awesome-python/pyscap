#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee, privilege, owner, table_name from dba_tab_privs
where (owner='SYS' or table_name like 'DBA_%')
and privilege <> 'EXECUTE'
and grantee not in
('PUBLIC',
'AQ_ADMINISTRATOR_ROLE',
'AQ_USER_ROLE',
'AURORA\$JIS\$UTILITY\$',
'OSE\$HTTP\$ADMIN',
'TRACESVR',
'CTXSYS',
'DBA',
'DELETE_CATALOG_ROLE',
'EXECUTE_CATALOG_ROLE',
'EXP_FULL_DATABASE',
'GATHER_SYSTEM_STATISTICS',
'HS_ADMIN_ROLE',
'IMP_FULL_DATABASE',
'LOGSTDBY_ADMINISTRATOR',
'MDSYS',
'ODM',
'OEM_MONITOR',
'OLAPSYS',
'ORDSYS',
'OUTLN',
'RECOVERY_CATALOG_OWNER',
'SELECT_CATALOG_ROLE',
'SNMPAGENT',
'SYSTEM',
'WKSYS',
'WKUSER',
'WMSYS',
'WM_ADMIN_ROLE',
'XDB',
'LBACSYS',
'PERFSTAT',
'XDBADMIN',
'ADM_PARALLEL_EXECUTE_TASK',
'APPQOSSYS',
'DBFS_ROLE',
'HS_ADMIN_SELECT_ROLE',
'ORACLE_OCM',
'SYSMAN')
and grantee not in
(select grantee from dba_role_privs where granted_role='DBA')
order by grantee;" | egrep -v -e '^NAME$' -e '^MEMBER$' -e '^VALUE$' -e '^-+$' -e 'rows selected\.$' -e '^$')
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Access to DBMS system tables and other configuration or metadata is not restricted to DBAs:
$e"
fi

