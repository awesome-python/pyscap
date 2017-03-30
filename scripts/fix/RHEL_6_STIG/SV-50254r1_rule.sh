#!/bin/bash

files=`rpm -Va 2>/dev/null | grep '^.....U' | awk '{print $NF}'`

for file in $files; do
	if [[ ! -e $file ]]; then
		echo Skipping non-existent file/dir $file
		continue
	fi
	pkg=`rpm -qf $file`
	echo "Fixing owner of file $file in package $pkg"
	rpm --setugids $pkg
done

