#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select username, account_status from dba_users
order by username;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "Unapproved inactive or expired database accounts have been found on the database:
$e"
fi
