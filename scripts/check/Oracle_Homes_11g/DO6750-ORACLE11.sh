#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select value from v\$parameter where name = 'sec_protocol_error_further_action';")
if [[ $q =~ DELAY || $q =~ DROP ]]; then
	fail "The Oracle SEC_PROTOCOL_ERROR_FURTHER_ACTION parameter is not set to a value of DELAY or
DROP: $q"
fi

pass
