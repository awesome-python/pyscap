#!/bin/bash

f=/etc/grub.conf
. lib/file.sh
backup_file $f || exit 1

sed 's/^\s\+kernel .*$/& audit=1/' $f > $f.new
mv -f $f.new $f
