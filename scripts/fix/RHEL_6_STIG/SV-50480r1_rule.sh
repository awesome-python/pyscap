#!/bin/bash

. lib/general.sh
. lib/file.sh

interfaces=$(
ip link show | while read line; do
	#echo $line
	if [[ "$line" =~ ^[0-9]+:\ [0-9a-zA-Z.-]+: ]]; then
		i=$(echo $line | sed 's/^[0-9]\+: \([0-9a-zA-Z.-]\+\):.*$/\1/')
		echo -n "$i "
	fi
done
)

for i in $interfaces; do
	#echo $i
	if [[ ! -f "/etc/sysconfig/network-scripts/ifcfg-$i" ]]; then
		echo Adding disabled interface configuration for interface $i.
		echo "BOOTPROTO=none" > "/etc/sysconfig/network-scripts/ifcfg-$i"
		echo "DEVICE=$i" >> "/etc/sysconfig/network-scripts/ifcfg-$i"
		echo "USERCTL=no" >> "/etc/sysconfig/network-scripts/ifcfg-$i"
		echo "ONBOOT=no" >> "/etc/sysconfig/network-scripts/ifcfg-$i"
	fi
	
	if [[ "x$(egrep "^BOOTPROTO=.*dhcp.*" /etc/sysconfig/network-scripts/ifcfg-$i)" != "x" ]]; then
		echo -n "Disable DHCP on interface $i? {yes/no} [no]: "
		read conf
		if [[ "x$conf" = "xyes" ]]; then
			backup_file "/etc/sysconfig/network-scripts/ifcfg-$i"
			sed 's/^BOOTPROTO=.*dhcp.*$/BOOTPROTO=none/' "/etc/sysconfig/network-scripts/ifcfg-$i" > "/etc/sysconfig/network-scripts/ifcfg-$i.new"
			mv -f "/etc/sysconfig/network-scripts/ifcfg-$i.new" "/etc/sysconfig/network-scripts/ifcfg-$i"
		fi
	fi
done
