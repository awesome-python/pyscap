#!/bin/bash

# this is the auditd.conf super fix
# add & uncomment the following line to files that change auditd.conf and add their fixes below
#sh fix/RHEL_6_STIG/auditd_conf.sh $f || exit 1

f=/etc/audit/auditd.conf
. lib/file.sh
backup_file $f || exit 1

r=`grep space_left_action $f`
if [[ "x$r" == "x" ]]; then
	echo 'space_left_action = email' >> $f
else
	sed 's/space_left_action\s*=\s*.*/space_left_action = email/i' $f > $f.new
	mv -f $f.new $f
fi

r=`grep disk_error_action $f`
if [[ "x$r" == "x" ]]; then
	echo 'disk_error_action = syslog' >> $f
else
	sed 's/^\s*disk_error_action\s*=\s*.*$/disk_error_action = syslog/' $f > $f.new
	mv -f $f.new $f
fi

r=`grep disk_full_action $f`
if [[ "x$r" == "x" ]]; then
	echo 'disk_full_action = email' >> $f
else
	sed 's/disk_full_action\s*=\s*[a-zA-Z]\+/disk_full_action = syslog/i' $f > $f.new
	mv -f $f.new $f
fi

r=`grep max_log_file_action $f`
if [[ "x$r" == "x" ]]; then
	echo 'max_log_file_action = rotate' >> $f
else
	sed 's/^\s*max_log_file_action\s*=\s*.*$/max_log_file_action = rotate/' $f > $f.new
	mv -f $f.new $f
fi

service auditd restart