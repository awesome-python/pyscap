#!/bin/bash

. lib/general.sh

ip link show | while read line; do
	#echo $line
	if [[ "$line" =~ ^[0-9]+:\ [0-9a-zA-Z.-]+: ]]; then
		i=$(echo $line | sed 's/^[0-9]\+: \([0-9a-zA-Z.-]\+\):.*$/\1/')
		#echo Interface $i
		if [[ ! -f "/etc/sysconfig/network-scripts/ifcfg-$i" ]]; then
			fail "$i is using default ifcfg"
		fi
		
		if [[ "x$(egrep "^BOOTPROTO=.*dhcp.*" /etc/sysconfig/network-scripts/ifcfg-$i)" != "x" ]]; then
			fail "$i is using dhcp"
		fi
	fi
done
pass
