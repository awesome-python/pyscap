#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select table_name from dba_tab_privs
where grantee='PUBLIC'
and privilege ='EXECUTE'
and table_name in
('UTL_FILE',
'UTL_SMTP',
'UTL_TCP',
'UTL_HTTP',
'DBMS_RANDOM',
'DBMS_LOB',
'DBMS_SQL',
'DBMS_SYS_SQL',
'DBMS_JOB',
'DBMS_BACKUP_RESTORE',
'DBMS_OBFUSCATION_TOOLKIT');")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	pass
fi

fail "Execute permission has not been revoked from PUBLIC for restricted Oracle packages:
$e"