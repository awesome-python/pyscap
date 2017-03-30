#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "A single database connection configuration file must not be used to configure all database clients"
else
	notchecked
fi

