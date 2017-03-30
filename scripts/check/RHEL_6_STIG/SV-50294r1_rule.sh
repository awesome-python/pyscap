#!/bin/bash

for i in `grep "^log_file" /etc/audit/auditd.conf|sed 's/^[^/]*//; s/[^/]*$//'`; do
	mode=`stat -c '%a' $i`
	if [ "$mode" -gt "0755" ]; then
		#echo "$i has mode $mode > 0755"
		echo "<result>fail</result><message>$i has mode $mode greater than 0755</message>"
		exit
	fi
done
	
echo '<result>pass</result>'