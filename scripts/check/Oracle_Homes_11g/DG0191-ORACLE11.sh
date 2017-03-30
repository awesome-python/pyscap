#!/bin/bash

. lib/oracle.sh
. lib/file.sh

q=$(sqlplus_sysdba "select value from v\$parameter where name = 'remote_login_passwordfile';")
if [[ $q =~ NONE ]]; then
	pass
elif [[ $q =~ SHARED ]]; then
	fail "Credentials used to access remote databases are not protected by encryption and restricted to authorized users"
elif [[ $q =~ EXCLUSIVE ]]; then
	# check permissions on orapw*.ora files
	error_if_no_ORACLE_HOME
	for i in $(find $ORACLE_HOME/dbs -name 'orapw*.ora'); do
		fail_if_world_readable $i
	done
fi

pass
