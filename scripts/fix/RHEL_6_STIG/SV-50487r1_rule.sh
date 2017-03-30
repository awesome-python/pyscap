#!/bin/bash

echo "This fix turns off forwarding. If this machine is routing you should leave this finding open."
echo -n "Continue? (y/n): [n]"
read r
if [[ "$r" != "y" ]]; then
	exit
fi

f=/etc/sysconfig/iptables
if [[ -f $f ]]; then
	. lib/file.sh
backup_file $f || exit 1
fi

echo Flushing FORWARD chain...
iptables -F FORWARD

echo Setting default policy to DROP packets...
iptables -P FORWARD DROP

echo Saving changes to $f.
iptables-save > $f