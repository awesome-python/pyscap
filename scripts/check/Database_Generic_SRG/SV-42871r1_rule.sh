#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# mysql doesn't encrypt at the database or table level, though encryption functions can be used at the field level & disk level

	echo '<result>fail</result><message>mysql does not encrypt at the database or table level</message>'
else
	echo '<result>notchecked</result>'
fi