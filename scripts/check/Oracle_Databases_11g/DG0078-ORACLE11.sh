#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username from dba_users
where username not in
('ANONYMOUS',
'APPQOSSYS',
'DBSNMP',
'DIP',
'MGMT_VIEW',
'ORACLE_OCM',
'OUTLN',
'SYS',
'SYSMAN',
'SYSTEM',
'WMSYS',
'XDB',
'XS\$NULL')
order by username;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Each database user, application or process should have an individually assigned account:
$e"
fi
