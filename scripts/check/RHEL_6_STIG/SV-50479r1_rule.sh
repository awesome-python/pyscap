#!/bin/bash
. lib/general.sh

l=$(egrep '^space_left\s*=\s*[0-9]+' /etc/audit/auditd.conf | cut -d'#' -f 1 | cut -d'=' -f 2)
#echo Space left: $l
if [[ "$l" -lt "75" ]]; then
	fail "The audit system must provide a warning when allocated audit record storage volume reaches a documented percentage of maximum audit record storage capacity: space_left is $l (MB) in /etc/audit/auditd.conf"
fi

pass