#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'remote_os_authent';")
if [[ ! "$e" =~ ^\s*FALSE\s*$ ]]; then
	fail "The Oracle REMOTE_OS_AUTHENT parameter is not set to FALSE:
$e"
fi

pass