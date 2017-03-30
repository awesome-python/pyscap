#!/bin/bash

for f in `find / -xdev -type f -perm -002 2>/dev/null`; do
	echo Changing permissions on $f
	chmod a-w $f
done
