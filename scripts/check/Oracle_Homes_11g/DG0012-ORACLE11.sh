#!/bin/bash

. lib/oracle.sh

q=`su -l oracle -c 'ls $ORACLE_BASE'`
for i in $q; do
	case $i in
		admin | cfgtoollogs | checkpoints | diag | fast_recovery_area | oradata | oraInventory | product)
			;;
		*)
			fail "Database software directories including DBMS configuration files are not stored in dedicated directories
separate from the host OS and other applications: unknown ORACLE_BASE entry: $i"
			;;
	esac
done
pass
