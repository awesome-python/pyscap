#!/bin/bash

. lib/oracle.sh

for i in $(oracle_listeners); do
	status=$(su -l oracle -c "lsnrctl status $i" | grep '^Security')
	if [[ $status =~ OFF ]]; then
		fail "The Oracle Listener is not configured to require administration authentication: Security = OFF"
	elif [[ $status =~ ON:\ Local\ OS\ Auth ]]; then
		continue
	elif [[ $status =~ ON:\ Password ]]; then
		fail "The Oracle Listener is not configured to require administration authentication: Security = On: Password..."
	else
		error "The Oracle Listener is not configured to require administration authentication: Unknown response from lsnrctl status: $status"
	fi
done

pass
