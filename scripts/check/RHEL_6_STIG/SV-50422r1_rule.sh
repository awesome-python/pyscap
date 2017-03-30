#!/bin/bash
. lib/general.sh

if [[ ! -s /etc/ntp.conf ]]; then
	fail "The system clock must be synchronized to an authoritative DoD time source: /etc/ntp.conf doesn't exit"
fi

if [[ "x$(egrep '^server\s' /etc/ntp.conf)" = "x" ]]; then
	fail "The system clock must be synchronized to an authoritative DoD time source: no servers are defined in /etc/ntp.conf"
fi

pass