#!/bin/bash

f=/etc/pam.d/system-auth
. lib/file.sh
backup_file $f || exit 1

r=`grep nullok $f`
if [[ "x$r" != "x" ]]; then
	cat $f | sed 's/\snullok//i' > $f.new
	mv -f $f.new $f
fi

r=`grep pam_cracklib $f`
if [[ "x$r" != "x" ]]; then
	# need to edit file, not insert
	cat $f | sed 's/^password\s\+\S\+\s\+pam_cracklib\.so.*$/password required pam_cracklib.so maxrepeat=3 ucredit=-1 ocredit=-1 lcredit=-1 difok=4 dcredit=-1/i' > $f.new
else
	cat $f | perl fix/insert_text.pl "password required pam_cracklib.so maxrepeat=3 ucredit=-1 ocredit=-1 lcredit=-1 difok=4 dcredit=-1\n" before '^password\s+include\s+system-auth-ac' > $f.new
fi
mv -f $f.new $f

r=`grep pam_unix $f`
if [[ "x$r" != "x" ]]; then
	# need to edit file, not insert
	cat $f | sed 's/^password\s\+\S\+\s\+pam_unix\.so.*$/password sufficient pam_unix.so sha512 remember=24/i' > $f.new
else
	cat $f | perl fix/insert_text.pl "password sufficient pam_unix.so sha512 remember=24\n" before '^session' > $f.new
fi
mv -f $f.new $f
