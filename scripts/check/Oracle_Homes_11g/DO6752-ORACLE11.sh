#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select value from v\$parameter where name = 'sec_protocol_error_trace_action';")
if [[ $q =~ NONE ]]; then
	fail "The Oracle SEC_PROTOCOL_ERROR_TRACE_ACTION parameter is set to NONE: $q"
elif [[ $q =~ TRACE || $q =~ LOG || $q =~ ALERT ]]; then
	pass
else
	error "The Oracle SEC_PROTOCOL_ERROR_TRACE_ACTION parameter is set to NONE: Unknown value $q"
fi
