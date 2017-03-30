#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>mysql does not support display of failed logins on login</message>'
else
	echo '<result>notchecked</result>'
fi
