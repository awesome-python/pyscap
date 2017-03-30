#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not use multifactor authentication for local access to privileged accounts.</message>'
else
	echo '<result>notchecked</result>'
fi