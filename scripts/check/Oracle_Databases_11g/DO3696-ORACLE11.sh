#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'resource_limit';")
if [[ ! "$e" =~ ^\s*TRUE\s*$  ]]; then
	fail "The Oracle RESOURCE_LIMIT parameter is not set to TRUE:
$e"
fi

pass