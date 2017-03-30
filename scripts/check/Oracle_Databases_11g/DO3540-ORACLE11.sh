#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'sql92_security';")
if [[ ! "$e" =~ ^\s*TRUE\s*$ ]]; then
	fail "The Oracle SQL92_SECURITY parameter should be set to TRUE:
$e"
fi

pass