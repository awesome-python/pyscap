#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select instance_name from v\$instance
where instance_name in ('XE',
'IASDB',
'ORCL',
'OEMREP',
'SID',
'ixos',
'ARIS',
'MSAM',
'VPX',
'OPENVIEW',
'OVO')
or instance_name like 'SA%'
or instance_name like 'CTM%';")
if [[ $e =~ 'no rows selected' ]]; then
	pass
fi

fail "The Oracle SID is the default SID:
$e"
