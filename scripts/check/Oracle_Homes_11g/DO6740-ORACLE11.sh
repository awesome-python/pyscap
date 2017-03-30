#!/bin/bash

. lib/oracle.sh

# The Oracle Listener ADMIN_RESTRICTIONS parameter is present and set to OFF

for i in $(oracle_listeners); do
	param_file=$(su -l oracle -c "lsnrctl status $i" | grep 'Listener Parameter File' | sed 's/^Listener Parameter File\s*\(.*\)$/\1/')
	if [[ "x$(grep -i "ADMIN_RESTRICTIONS_$i\s*=\s*ON" $param_file)" = "x" ]]; then
		fail "The Oracle Listener ADMIN_RESTRICTIONS parameter is present and set to OFF"
	fi
done

pass
