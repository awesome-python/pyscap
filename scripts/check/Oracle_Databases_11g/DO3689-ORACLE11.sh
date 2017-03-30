#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select owner ||'.'|| table_name ||':'|| privilege from dba_tab_privs
where grantee = 'PUBLIC'
and owner not in
('SYS',
'CTXSYS',
'MDSYS',
'ODM',
'OLAPSYS',
'MTSSYS',
'ORDPLUGINS',
'ORDSYS',
'SYSTEM',
'WKSYS',
'WMSYS',
'XDB',
'LBACSYS',
'PERFSTAT',
'SYSMAN',
'DMSYS',
'EXFSYS',
'DBSNMP');")
if [[ "x$e" != $'x\nno rows selected'  ]]; then
	fail "Object permissions granted to PUBLIC are not restricted:
$e"
fi

pass