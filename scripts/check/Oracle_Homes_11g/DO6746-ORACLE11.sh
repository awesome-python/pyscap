#!/bin/bash

. lib/oracle.sh

# The Oracle Listener ADMIN_RESTRICTIONS parameter is present and set to OFF

for i in $(oracle_listeners); do
	param_file=$(su -l oracle -c "lsnrctl status $i" | grep 'Listener Parameter File' | sed 's/^Listener Parameter File\s*\(.*\)$/\1/')
	r=$(grep -Pizo '\(HOST\s*=\s*[a-z.0-9]+\)' $param_file | wc -l)
	q=$(grep -Pizov '\(HOST\s*=\s*[.0-9]+\)' $param_file | wc -l)
	if [[ "$r" != "$q" ]]; then
		fail "The Oracle listener.ora file does not specify IP addresses rather than host names to identify hosts: $(grep -Pizo '\(HOST\s*=\s*[a-z.0-9]+\)' $param_file)"
	fi
done

pass
