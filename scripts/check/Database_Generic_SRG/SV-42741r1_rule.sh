#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must support enforcement of logical access restrictions associated with changes to the DBMS configuration and to the database itself"
else
	notchecked
fi

