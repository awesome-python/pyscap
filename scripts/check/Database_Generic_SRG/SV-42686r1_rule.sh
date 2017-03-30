#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS must validate the binding of the information to the identity of the information producer.</message>'
else
	echo '<result>notchecked</result>'
fi