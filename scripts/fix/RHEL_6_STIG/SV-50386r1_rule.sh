#!/bin/bash

f=/etc/grub.conf
. lib/file.sh
backup_file $f || exit 1

echo "Enter a password to protect system boot with grub:"
grub-crypt --sha-512 > grub_password_hash.txt || exit 1

pw=`cat grub_password_hash.txt`
pw="password --encrypted $pw"

cat $f | perl fix/insert_text.pl "$pw\n" after ! '^#' > $f.new || exit 1
mv -f $f.new $f

rm -f grub_password_hash.txt