#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME
e=$(sqlplus_sysdba "select value from v\$parameter where name = 'audit_trail';")

# - User ID.
# - Successful and unsuccessful attempts to access security files
# - Date and time of the event.
# - Type of event.
if [[ "x$e" =~ "NONE" ]]; then
	fail "Audit records do not contain required information: audit_trail set to NONE"
else
	# any other setting is ok
	pass
fi
