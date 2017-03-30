#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not support the requirement to activate an alarm and/or automatically shut down the information system if an application component failure is detected: not supported</message>'
else
	echo '<result>notchecked</result>'
fi