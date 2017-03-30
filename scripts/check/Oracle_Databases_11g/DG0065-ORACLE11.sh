#!/bin/bash

. lib/oracle.sh

fail_if_no_wallet
fail_if_no_listener_ssl

e=$(sqlplus_sysdba "select username from dba_users
where authentication_type = 'PASSWORD'
order by username;")
if [[ $e =~ 'no rows selected' ]]; then
	pass
else
	fail "DBMS authentication should require use of a DoD PKI certificate. Accounts with standard password authentication:
$e";
fi
