#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "The DBMS must employ cryptographic mechanisms preventing the unauthorized disclosure of information at rest unless the data is otherwise protected by alternative physical measures: not supported"
else
	notchecked
fi
