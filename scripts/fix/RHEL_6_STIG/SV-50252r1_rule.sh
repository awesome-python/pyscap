#!/bin/bash

files=`rpm -Va 2>/dev/null | grep '^.M' | awk '{print $NF}'`
packages=''
for f in $files; do
	p=`rpm -qf $f`
	echo Found $f in package $p
	r=`echo "$packages" | grep $p`
	if [[ "x$r" == "x" ]]; then
		echo Need to reset permissions on package $p
		packages="$packages $p"
	fi
done

for p in $packages; do
	echo Re-setting permissions on package $p
	rpm --setperms $p
done
