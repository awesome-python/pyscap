#!/bin/bash

. lib/general.sh

r=`grep -R uvscan /etc/cron* /var/spool/cron/* 2>/dev/null`
if [[ "x$r" == "x" ]]; then
	fail 'uvscan is not listed in cron files'
fi

d=/usr/local/uvscan
if [[ ! -d $d ]]; then
	fail "$d does not exist"
fi

if [[ ! -f $d/avvscan.dat || ! -f $d/avvnames.dat || ! -f $d/avvclean.dat ]]; then
	fail "No virus definition files are in $d"
fi

cre=$(uvscan --version | grep 'Dat set' | cut -d' ' -f 6-8 | sed 's/\ /-/g')
cre_secs=$(date -d "$cre" +%s)
now_secs=$(date +%s)

if [[ $[$now_secs - $cre_secs] -gt $[7 * 24 * 60 * 60] ]]; then
	fail "uvscan virus definitions are older than 7 days: created $cre"
fi

# if [[ "x$(find /usr/local/uvscan \( -name avvscan.dat -or -name avvnames.dat -or -name avvclean.dat \) -and -mtime +7)" != "x" ]]; then
	# fail "uvscan virus definitions are older than 7 days"
# fi

pass
