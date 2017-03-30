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
# - Data required to audit the possible use of covert channel mechanisms.
# - Privileged activities and other system-level access.
# - Starting and ending time for access to the system.
# - Security relevant actions associated with periods processing or the changing of security labels or
# categories of information.
fail_if_ols_not_installed
if [[ "x$e" =~ "DB" && "x$e" =~ "EXTENDED" ]]; then
	pass
else
	fail "Audit records do not contain required information: audit_trail not set to DB and EXTENDED"
fi
