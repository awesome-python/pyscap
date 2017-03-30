#!/bin/bash

. lib/general.sh

a=`iptables-save | egrep '^:INPUT\s+DROP' 2>/dev/null`
if [[ "x$a" == "x" ]]; then
        fail 'default policy for INPUT chain is not DROP'
fi

a=`egrep '^:INPUT\s+DROP' /etc/sysconfig/iptables 2>/dev/null`
if [[ "x$a" == "x" ]]; then
	fail 'default startup policy for INPUT chain is not DROP'
fi

pass
