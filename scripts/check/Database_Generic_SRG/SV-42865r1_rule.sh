#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# mysql in auto-commit mode, the default, treats an entire client connection as a transaction

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi