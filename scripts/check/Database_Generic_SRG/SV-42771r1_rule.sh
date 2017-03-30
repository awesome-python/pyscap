#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Database recovery procedures must be developed, documented, implemented, and periodically tested"
else
	notchecked
fi

