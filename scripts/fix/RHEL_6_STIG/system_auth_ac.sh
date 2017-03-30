#!/bin/bash

f=/etc/pam.d/system-auth-ac
. lib/file.sh
backup_file $f || exit 1

r=`grep nullok $f`
if [[ "x$r" != "x" ]]; then
	cat $f | sed 's/\snullok//i' > $f.new
	mv -f $f.new $f
fi

r=`grep pam_faillock $f`
if [[ "x$r" != "x" ]]; then
	echo 'TODO need to edit file, not insert'
	exit 1
else
	cat $f | perl fix/insert_text.pl "auth [default=die] pam_faillock.so authfail deny=3 unlock_time=604800 fail_interval=900\nauth required pam_faillock.so authsucc deny=3 unlock_time=604800 fail_interval=900\n" before ! '^(#|auth)' > $f.new
fi
mv -f $f.new $f
