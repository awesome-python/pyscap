#!/bin/bash

for i in '/lib' '/lib64' '/usr/lib' '/usr/lib64' '/lib/modules'
do
	r=`find -L "$i" -perm /022 2>/dev/null`
	for f in $r; do
		if [[ -L $f ]]; then
			if [[ -e $f ]]; then
				chmod go-w $f
			else
				echo "Skipping broken link $f"
			fi
		else
			chmod go-w $f
		fi
	done
done

