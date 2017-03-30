#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee, granted_role from dba_role_privs
where grantee not in
('DATAPUMP_EXP_FULL_DATABASE',
'DATAPUMP_IMP_FULL_DATABASE',
'DBA',
'DBSNMP',
'EXECUTE_CATALOG_ROLE',
'EXP_FULL_DATABASE',
'HS_ADMIN_ROLE',
'IMP_FULL_DATABASE',
'LOGSTDBY_ADMINISTRATOR',
'MGMT_VIEW',
'OEM_MONITOR',
'ORACLE_OCM',
'OUTLN',
'PUBLIC',
'SELECT_CATALOG_ROLE',
'SYS',
'SYSMAN',
'SYSTEM',
'WMSYS',
'XDB');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Developers should not be assigned excessive privileges on production databases:
$e"
fi

