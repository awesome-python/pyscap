#!/bin/bash

f='/etc/securetty'
. lib/file.sh
backup_file $f || exit 1

egrep -v '^vc/[0-9]+$' $f > $f.new
mv -f $f.new $f
