#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not employ automated mechanisms to alert security personnel of inappropriate or unusual activities with security implications: not supported</message>'
else
	echo '<result>notchecked</result>'
fi