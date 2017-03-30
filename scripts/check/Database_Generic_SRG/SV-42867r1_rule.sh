#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>notapplicable</result>'
else
	echo '<result>notchecked</result>'
fi
