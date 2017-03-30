#!/bin/bash

# The DBMS must prevent access to organization defined security-relevant information except during secure, non-operable system states.
	
. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# mysql uses in band management
	echo '<result>fail</result><message>mysql does not support out of band management</message>'
else
	echo '<result>notchecked</result>'
fi