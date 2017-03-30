#!/bin/bash

. lib/oracle.sh
. lib/general.sh

fail_if_no_ORACLE_HOME
q=$(sqlplus_sysdba "select banner from v\$version where banner like 'Oracle%';")

# From http://www.oracle.com/us/support/library/lifetime-support-technology-069183.pdf

# compare support dates
d1=`date '+%Y%m%d'`
if [[ $q =~ (12\.1\.[0-9]+\.[0-9]+\.[0-9]+) ]]; then
	d2=`date -d '31 Jul 2018' '+%Y%m%d'`
	if [[ "$d1" -gt "$d2" ]]; then
		fail "$q is no longer supported"
	else
		pass
	fi
elif [[ $q =~ (11\.2\.[0-9]+\.[0-9]+\.[0-9]+) ]]; then
	d2=`date -d '31 Jan 2015' '+%Y%m%d'`
	if [[ "$d1" -gt "$d2" ]]; then
		fail "$q is no longer supported"
	else
		pass
	fi
else
	fail "Unsupported or unknown version: $q"
fi