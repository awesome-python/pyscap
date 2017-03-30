#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select owner from dba_tables where table_name = 'AUD\$';")
if [[ "x$e" == "xSYSTEM" || "x$e" == "xSYS" ]]; then
	pass
fi

fail "The audit table is not owned by SYS or SYSTEM:
$e"