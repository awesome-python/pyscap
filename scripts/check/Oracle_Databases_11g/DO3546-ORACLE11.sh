#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select value from v\$parameter where name = 'remote_login_passwordfile';")
if [[ ! "$e" =~ ^\s*EXCLUSIVE\s*$ && ! "$e" =~ ^\s*NONE\s*$ ]]; then
	fail "The Oracle REMOTE_LOGIN_PASSWORDFILE parameter is not set to EXCLUSIVE or NONE:
$e"
fi

pass