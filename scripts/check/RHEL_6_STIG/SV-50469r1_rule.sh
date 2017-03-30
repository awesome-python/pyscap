#!/bin/bash

for i in `grep -l control-alt-delete /etc/init/* 2>/dev/null`; do
	r=`grep '^exec' $i 2>/dev/null | grep shutdown`
	if [[ "x$r" != "x" ]]; then
		echo '<result>fail</result><message>Pressing Control-Alt-Delete shuts down or restarts the system</message>'
		exit
	fi
done

echo '<result>pass</result>'