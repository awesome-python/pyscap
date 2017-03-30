#!/bin/bash

check_del() {
	if [[ -z "$@" ]]; then
		return
	fi

	echo "Found the following old files: $@"
	rm -I $@
}

ORACLE_BASE=`su -l oracle -c 'echo $ORACLE_BASE'`
find_opts=" -mtime +14" # older than 14 days
sids=`grep -v -e '^\s*#' -e '^\s*$' < /etc/oratab | cut -d: -f1`

for sid in $sids; do
	db=$sid
	ORACLE_HOME=`grep -v -e '^\s*#' -e '^\s*$' < /etc/oratab | grep $sid | cut -d: -f2`
	
	# archive files
	files=`find $ORACLE_BASE/fast_recovery_area/${sid^^}/archivelog -name '*.arc' $find_opts | xargs echo`
	check_del $files
	
	# sys audit files
	files=`find $ORACLE_BASE/admin/$sid/adump -name "${sid}_ora_*.aud" -or -name "${sid}_ora_*.xml" $find_opts | xargs echo`
	check_del $files

	# audit files
	files=`find $ORACLE_HOME/rdbms/audit -name "${sid}_ora_*.aud" -or -name "${sid}_ora_*.xml" $find_opts | xargs echo`
	check_del $files
	
	# trace files (old background and user dumps aka bdump and udump)
	files=`find $ORACLE_BASE/diag/rdbms/$db/$sid/trace -name "${sid}_*.trc" -or -name "${sid}_*.trm" $find_opts | xargs echo`
	check_del $files

	# core dump files (aka cdump)
	files=`find $ORACLE_BASE/diag/rdbms/$db/$sid/cdump -name "${sid}_*.trc" -or -name "${sid}_*.trm" $find_opts | xargs echo`
	check_del $files

	# listener core dumps
	files=`find $ORACLE_BASE/diag/tnslsnr/*/listener/cdump -name "${sid}_*.trc" -or -name "${sid}_*.trm" $find_opts | xargs echo`
	check_del $files
	
	# client logs
	files=`find $ORACLE_HOME/log/*/client -name "clsc*.log" $find_opts | xargs echo`
	check_del $files
done
