#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>Databases utilizing Discretionary Access Control (DAC) must enforce a policy that limits propagation of access rights.</message>'
else
	echo '<result>notchecked</result>'
fi