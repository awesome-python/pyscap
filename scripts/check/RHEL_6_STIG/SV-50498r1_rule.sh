#!/bin/bash

for i in `mount -t ext2,ext3,ext4,msdos,umsdos,vfat | awk '{print $3}'`; do
	#echo Checking $i
	r=`find $i -xdev -type d -perm 002 ! -perm 1000 2>/dev/null`
	if [[ "x$r" != "x" ]]; then
		echo "<result>fail</result><message>Sticky bit is not set on public directories: $r on $i</message>"
		exit
	fi
done

echo '<result>pass</result>'
