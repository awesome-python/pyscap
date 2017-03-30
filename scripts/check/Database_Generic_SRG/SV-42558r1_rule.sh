#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Non-privileged accounts must be utilized when accessing non-administrative functions"
else
	notchecked
fi

