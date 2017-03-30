#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# mysql returns the thread id for connection_id(), which will be unique for current connections

	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi