#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select owner||'.'||name from dba_source
where line=1 and owner not in
('CTXSYS',
'DBSNMP',
'MDSYS',
'ODM',
'OE',
'OLAPSYS',
'ORACLE_OCM',
'ORDPLUGINS',
'ORDSYS',
'OUTLN',
'PM',
'QS_ADM',
'RMAN',
'SYS',
'SYSMAN',
'SYSTEM',
'WKSYS',
'WMSYS',
'XDB')
and owner not like 'OEM%'
and text not like '%wrapped%'
and type in ('PROCEDURE', 'FUNCTION', 'PACKAGE BODY');")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Developers should not be assigned excessive privileges on production databases:
$e"
fi
