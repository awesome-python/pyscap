#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	mysql_fail_audits_not_added 'The DBMS does not produce audit records containing sufficient information to establish the sources (origins) of the events.'
	
	pass
else
	notchecked
fi
