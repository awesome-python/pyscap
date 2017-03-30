#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "DBMS backup and restoration files must be protected from unauthorized access"
else
	notchecked
fi

