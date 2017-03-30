#!/bin/bash

. lib/oracle.sh

v=$(sqlplus_sysdba "select version from v\$instance;")
if [[ ! $v =~ 11\. ]]; then
	error "Only support Oracle 11: $v"
fi

e=$(sqlplus_sysdba "select instance_name from v\$instance;")
pat='11(.\d+)*'
for i in $e; do
	#echo "testing $i"
	if [[ $i =~ $pat ]]; then
		fail "Oracle instance names contain Oracle version numbers: $i"
	fi
done

pass
