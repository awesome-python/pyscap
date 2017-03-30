#!/bin/bash

for i in `mount -t ext2,ext3,ext4,msdos,umsdos,vfat | awk '{print $3}'`; do
	#echo Checking $i
	r=`find $i -xdev -type d -perm 0002 -uid +500 -print`
	if [[ "x$r" != "x" ]]; then
		echo "<result>fail</result>User owned world writable directory: $r on $i"
		exit
	fi
done

echo '<result>pass</result>'
