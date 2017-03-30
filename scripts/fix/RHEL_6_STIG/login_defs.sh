#!/bin/bash

# this is the login.defs super fix
# add & uncomment the following line to files that change login.defs and add their fixes below
#sh fix/RHEL_6_STIG/login_defs.sh || exit 1

f=/etc/login.defs
. lib/file.sh
backup_file $f || exit 1

cat $f | sed -e 's/^PASS_MIN_LEN\s\+[0-9]\+$/PASS_MIN_LEN 14/i' -e 's/^PASS_MIN_DAYS\s\+[0-9]\+$/PASS_MIN_DAYS 1/i' -e 's/^PASS_MAX_DAYS\s\+[0-9]\+$/PASS_MAX_DAYS 60/i' -e 's/^UMASK\s\+[0-9]\+/UMASK 077/' > $f.new

mv -f $f.new $f
