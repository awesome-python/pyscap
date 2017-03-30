#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME
e=$(sqlplus_sysdba "select value from v\$parameter where name = 'audit_trail';")

# - User ID.
# - Successful and unsuccessful attempts to access security files
# - Date and time of the event.
# - Type of event.
# - Success or failure of event.
# - Successful and unsuccessful logons.
# - Denial of access resulting from excessive number of logon attempts.
# - Blocking or blacklisting a user ID, terminal or access port, and the reason for the action.
# - Activities that might modify, bypass, or negate safeguards controlled by the system.
if [[ "x$e" =~ "DB" || "x$e" =~ "XML" ]]; then
	pass
else
	fail "Audit records do not contain required information: audit_trail not set to DB or XML"
fi
