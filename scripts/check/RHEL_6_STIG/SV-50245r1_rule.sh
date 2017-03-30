#!/bin/bash

for i in `egrep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//`; do
	mode=`stat -c '%G' $i`
	if [ "$mode" != "root" ]; then
		echo "<result>fail</result><message>Group-owner of $i is not root</message>"
		exit
	fi
done
	
echo '<result>pass</result>'