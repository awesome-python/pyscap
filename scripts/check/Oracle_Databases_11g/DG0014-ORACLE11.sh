#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username from dba_users where username in
('ALLUSERS',
'AOLDEMO',
'AQDEMO',
'AQJAVA',
'AQUSER',
'AUC_GUEST',
'BI',
'CTXDEMO',
'DEMO8',
'DEV2000_DEMOS',
'HR',
'IX',
'OE',
'ORABAMSAMPLES',
'PM',
'PORTAL_DEMO',
'PORTAL30_DEMO',
'QS',
'SCOTT',
'SECDEMO',
'SH',
'WK_TEST')
or username like 'QS_%';")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Default demonstration and sample database objects and applications not removed:
$e";
fi
