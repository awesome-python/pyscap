#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not alert designated organizational officials in the event of an audit processing failure.</message>'
else
	echo '<result>notchecked</result>'
fi