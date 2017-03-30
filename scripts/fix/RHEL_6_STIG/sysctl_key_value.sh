#!/bin/bash

if [[ "x$1" == "x" || "x$2" == "x" ]]; then
	echo "Usage: $0 key value"
	exit 1
fi

f=/etc/sysctl.conf
. lib/file.sh
backup_file "$f" || exit 1

echo "Adding setting to running kernel"
sysctl -w "$1=$2"

echo "Saving setting to sysctl.conf"
r=`grep -i '^$1' $f`
if [[ "x$r" == "x" ]]; then
	echo "$1 = $2" >> $f
else
	sed "s/$1\s\+=\s\+.*/$1 = $2/i" $f > $f.new
	mv -f $f.new $f
fi

