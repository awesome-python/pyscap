#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS must support the organizational requirement to employ automated mechanisms for enforcing access restrictions.</message>'
else
	echo '<result>notchecked</result>'
fi