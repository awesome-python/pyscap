#!/bin/bash

. lib/oracle.sh

members=`cat /etc/group | grep -i dba | cut -d: -f4`
if [[ $members =~ root ]]; then
	fail "Unnecessary privileges to the host system have been granted to DBA OS accounts: root is a dba member"
fi

int=$(word_intersection "$(groups root | cut -d: -f2)" "$members")
if [[ ! $int =~ ^\s*$ ]]; then
	fail "Unnecessary privileges to the host system have been granted to DBA OS accounts: a root group is a dba member"
fi

for i in $members; do
	for g in $(groups $i | cut -d: -f2); do
		if [[ ! $g =~ ^(dba|oinstall)$ ]]; then
			fail "Unnecessary privileges to the host system have been granted to DBA OS accounts: $i belongs to $g"
		fi
	done
done

pass