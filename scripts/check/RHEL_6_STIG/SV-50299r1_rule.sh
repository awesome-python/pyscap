#!/bin/bash

for i in `grep "^log_file" /etc/audit/auditd.conf|sed s/^[^\/]*//`; do
	mode=`stat -c '%a' $i`
	if [ "$mode" -gt "0640" ]; then
		#echo "$i has mode $mode > 0640"
		echo "<result>fail</result><message>$i has mode $mode > 0640</message>"
		exit
	fi
done
	
echo '<result>pass</result>'
