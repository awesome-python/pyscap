#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# mysql doesn't support security labels
	echo '<result>fail</result><message>mysql does not support security labels</message>'
else
	echo '<result>notchecked</result>'
fi