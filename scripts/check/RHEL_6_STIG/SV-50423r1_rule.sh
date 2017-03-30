#!/bin/bash
. lib/general.sh

if [[ "x$(alternatives --display mta | grep 'link currently' | grep 'sendmail.postfix')" != "x" ]]; then
	# using postfix
	r=`egrep -i '^inet_interfaces\s*=\s*localhost' /etc/postfix/main.cf`
	if [[ "x$r" == "x" ]]; then
		fail "Mail relaying must be restricted: postfix not restricted to localhost"
	fi
elif [[ "x$(alternatives --display mta | grep 'link currently' | grep 'sendmail.sendmail')" != "x" ]]; then
	# using sendmail
	if [[ "x$(egrep -i '^DaemonPortOptions.*Addr=localhost' /etc/mail/sendmail.cf)" = "x" ]]; then
		fail "Mail relaying must be restricted: sendmail not restricted to localhost"
	fi
else
	fail "Mail relaying must be restricted: System is using an unknown MTA: $(alternatives --display mta | grep 'link currently')"
fi
pass
