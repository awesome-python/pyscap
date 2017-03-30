#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	fail "Vendor supported software must be evaluated and patched against newly found vulnerabilities"
else
	notchecked
fi

