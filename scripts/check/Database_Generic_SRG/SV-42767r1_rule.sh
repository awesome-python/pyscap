#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Recovery procedures and technical system features must exist to ensure recovery is done in a secure and verifiable manner"
else
	notchecked
fi

