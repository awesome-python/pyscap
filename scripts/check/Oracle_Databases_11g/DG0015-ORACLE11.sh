#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "set wrap off;
select created, owner, object_name, object_type
from dba_objects
where owner not in
('SYS',
'SYSTEM',
'ORDSYS',
'XDB',
'OLAPSYS',
'ODM',
'OUTLN',
'ORACLE_OCM',
'APPQOSSYS',
'DBSNMP',
'WMSYS',
'SYSMAN')
and object_type <> 'SYNONYM'
order by created, owner, object_name;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Database applications are not restricted from using static DDL statements to modify the application schema:
$e";
fi
