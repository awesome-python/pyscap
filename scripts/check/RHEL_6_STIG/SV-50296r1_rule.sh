#!/bin/bash

for i in `grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//`; do
	mode=`stat -c '%U' $i`
	if [ "$mode" != "root" ]; then
		#echo "$i is owned by $mode, not root"
		echo "<result>fail</result><message>$i is owned by $mode, not root</message>"
		exit
	fi
done

echo '<result>pass</result>'
