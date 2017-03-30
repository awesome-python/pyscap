#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select distinct owner, tablespace_name
from dba_tables
where owner not in
('APPQOSSYS',
'DBSNMP',
'OUTLN',
'SYS',
'SYSMAN',
'SYSTEM',
'WMSYS',
'XDB')
and tablespace_name is not NULL
and (owner, table_name) not in
(select owner, table_name from dba_external_tables)
order by tablespace_name;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
fi

fail "Application owner accounts do not have a dedicated application tablespace:
$e"
