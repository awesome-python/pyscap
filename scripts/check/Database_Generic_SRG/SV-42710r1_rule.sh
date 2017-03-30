#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_fail_audits_not_added 'The DBMS must produce audit records containing sufficient information to establish the outcome (success or failure) of the events.'
	
	pass
else
	notchecked
fi
