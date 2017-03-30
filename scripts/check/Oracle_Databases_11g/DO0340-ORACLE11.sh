#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee, granted_role from dba_role_privs
where default_role='YES'
and granted_role in
(select grantee from dba_sys_privs where upper(privilege) like '%USER%')
and grantee not in
('DBA',
'SYS',
'SYSTEM',
'CTXSYS',
'DBA',
'IMP_FULL_DATABASE',
'MDSYS',
'SYS',
'WKSYS',
'DATAPUMP_IMP_FULL_DATABASE')
and grantee not in (select distinct owner from dba_tables)
and grantee not in
(select distinct username from dba_users where upper(account_status) like
'%LOCKED%');")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	pass
fi

fail "Oracle application administration roles are enabled and not required or authorized:
$e"