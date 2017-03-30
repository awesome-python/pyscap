#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS itself, or the logging or alerting mechanism the application utilizes, do not provide a warning when allocated audit record storage volume reaches an organization defined percentage of maximum audit record storage capacity</message>'
else
	echo '<result>notchecked</result>'
fi