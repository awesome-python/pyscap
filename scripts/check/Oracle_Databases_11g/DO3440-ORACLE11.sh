#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select grantee from dba_role_privs
where granted_role='DBA'
and grantee not in
('SYS',
'SYSTEM',
'SYSMAN',
'CTXSYS',
'WKSYS');")
if [[ "x$e" = $'x\nno rows selected' ]]; then
	pass
fi

fail "The DBA role has been granted to unauthorized user accounts:
$e"