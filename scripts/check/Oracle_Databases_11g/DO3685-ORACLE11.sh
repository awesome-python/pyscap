#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'O7_dictionary_accessibility';")
if [[ "x$e" != $'x\nno rows selected' && ! "$e" =~ ^\s*FALSE\s*$  ]]; then
	fail "The Oracle O7_DICTIONARY_ACCESSIBILITY parameter is not set to FALSE:
$e"
fi

pass