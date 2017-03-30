#!/bin/bash

. lib/oracle.sh

q=$(sqlplus_sysdba "select value from v\$parameter where name = 'sec_case_sensitive_logon';")
if [[ ! $q =~ TRUE ]]; then
	fail "Case sensitivity for passwords is not enabled"
fi

pass
