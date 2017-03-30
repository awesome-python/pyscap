#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must have its auditing configured to reduce the likelihood of storage capacity being exceeded"
else
	notchecked
fi

