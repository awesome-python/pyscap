#!/bin/bash

files=`rpm -Va | grep '^......G' | awk '{print $NF}'`

for file in $files; do
	if [[ ! -e $file ]]; then
		echo "Group-owner can't be fixed on non-existent file $file"
		continue
	fi
	pkg=`rpm -qf $file`
	echo "Fixing group of file $file in package $pkg"
	rpm --setugids $pkg
done

