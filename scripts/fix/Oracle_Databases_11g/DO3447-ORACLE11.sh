#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username from dba_users where AUTHENTICATION_TYPE='EXTERNAL';")
if [[ "x$e" != $'x\nno rows selected' ]]; then
	echo "Users currently using EXTERNAL authentication; remove users before changing the prefix they log in with: $e"
	exit 1
fi

sqlplus_sysdba "alter system set os_authent_prefix = '' scope = spfile;"

restart_oracle