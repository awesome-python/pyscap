#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>mysql does not supprot failed login attempt listing on login</message>'
else
	echo '<result>notchecked</result>'
fi
