#!/bin/bash
. lib/general.sh

if [[ "x$(alternatives --display mta | grep 'link currently' | grep 'sendmail.postfix')" != "x" ]]; then
	# using postfix
	for i in `postconf alias_maps 2>/dev/null | cut -d: -f2`; do
		r=`postmap -q root $i 2>/dev/null`
		if [[ "x$r" == "x" ]]; then
			fail "The mail system must forward all mail for root to one or more system administrators: Mail is not being forwarded for root"
		fi
	done
elif [[ "x$(alternatives --display mta | grep 'link currently' | grep 'sendmail.sendmail')" != "x" ]]; then
	# using sendmail
	if [[ "x$(praliases | egrep '^root:')" = "x" ]]; then
		fail "The mail system must forward all mail for root to one or more system administrators: Mail is not being forwarded for root"
	fi
else
	fail "The mail system must forward all mail for root to one or more system administrators: System is using an unknown MTA: $(alternatives --display mta | grep 'link currently')"
fi

pass
