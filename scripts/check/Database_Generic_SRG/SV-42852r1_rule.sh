#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS must prevent the presentation of information system management-related functionality at an interface utilized by general (i.e., non-privileged) users.</message>'
else
	echo '<result>notchecked</result>'
fi