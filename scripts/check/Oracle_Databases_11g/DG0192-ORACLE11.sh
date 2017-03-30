#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'global_names';")
if [[ "$e" =~ "FALSE" ]]; then
	fail "Remote database or other external access do not use fully-qualified names"
fi

pass