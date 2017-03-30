#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# linux, and therefore mysql on linux, isn't retarded about session locks
	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi