#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username from dba_users
where (default_tablespace = 'SYSTEM' or temporary_tablespace = 'SYSTEM')
and username not in 
('MGMT_VIEW',
'OUTLN',
'SYS',
'SYSTEM');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
fi

fail "Access to the Oracle SYS and SYSTEM accounts is not restricted to authorized DBAs:
$e"