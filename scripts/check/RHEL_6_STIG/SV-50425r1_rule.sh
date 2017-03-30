#!/bin/bash
e=`grep logrotate /var/log/cron*`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>logrotate is not being used in any crontabs</message>'
	exit
fi

e=`ls /etc/cron.daily | grep logrotate`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>cron.daily is not using logrotate</message>'
	exit
fi

echo '<result>pass</result>'