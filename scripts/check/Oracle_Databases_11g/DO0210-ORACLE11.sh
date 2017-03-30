#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select count(*) from all_tables
where table_name like 'REPCAT%';")
if [[ "x$e" == "x0" ]]; then
	# Oracle Replication is not installed
	pass
fi

f=$(sqlplus_sysdba "select count(*) from sys.dba_repcatlog;")
pat='^\s+0$'
if [[ $f =~ $pat ]]; then
	# Oracle Replication is not in use
	pass
fi

fail "Access to default accounts used to support replication are not restricted to authorized DBAs:
$e
$f"

