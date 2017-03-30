#!/bin/bash

tar_rotate() {
	tar_file=$1
	log_files=$2
	#tar_opts="-p"
	tar_opts="-v -p"
	rotations=7
	
	tar -uf $tar_file $tar_opts $log_files 2>/dev/null
	if [ $? -eq 0 ]; then
		for (( i = $((rotations - 1)); i >= 1; i-- )); do
			if [ -f "$tar_file.gz.$i" ]; then
				#echo Rotatating $tar_file.gz.$i to $tar_file.gz.$((i+1))
				mv -f $tar_file.gz.$i $tar_file.gz.$((i+1))
			#else
				#echo $tar_file.gz.$i doesnt exist
			fi
		done
		if [ -f $tar_file.gz ]; then
			#echo Rotating $tar_file.gz to $tar_file.gz.1
			mv -f $tar_file.gz $tar_file.gz.1
		fi
	
		#echo Tar successful, Removing log files: $log_files...
		rm -f $log_files
		
		#echo Compressing tar...
		gzip $tar_file
	fi
}

ORACLE_BASE=`su -l oracle -c 'echo $ORACLE_BASE'`
find_opts=" -mtime +7" # older than 7 days
sids=`grep -v -e '^\s*#' -e '^\s*$' < /etc/oratab | cut -d: -f1`

for sid in $sids; do
	db=$sid
	ORACLE_HOME=`grep -v -e '^\s*#' -e '^\s*$' < /etc/oratab | grep $sid | cut -d: -f2`
	log_dir=/var/log/oracle/$sid
	
	mkdir -p $log_dir
	
	# listener logs, have to stop & start listener
	# COULD INTERRUPT SERVICES!
	su -l oracle -c 'lsnrctl stop'
	if [ $? -eq 0 ]; then
		tar_rotate $log_dir/listener.tar "$ORACLE_HOME/listener.log $(ls $ORACLE_BASE/diag/tnslsnr/*/listener/alert/log.xml)"
		touch $files
	fi
	su -l oracle -c 'lsnrctl start'

	# archive files
	files=`find $ORACLE_BASE/fast_recovery_area/${sid^^}/archivelog -name '*.arc' $find_opts | xargs echo`
	tar_rotate $log_dir/archivelogs.tar $files
	
	# sys audit files
	files=`find $ORACLE_BASE/admin/$sid/adump -name "${sid}_ora_*.aud" -or -name "${sid}_ora_*.xml" $find_opts | xargs echo`
	tar_rotate $log_dir/audits.tar $files

	# audit files
	files=`find $ORACLE_HOME/rdbms/audit -name "${sid}_ora_*.aud" -or -name "${sid}_ora_*.xml" $find_opts | xargs echo`
	tar_rotate $log_dir/audits.tar $files
	
	# trace files (old background and user dumps aka bdump and udump)
	files=`find $ORACLE_BASE/diag/rdbms/$db/$sid/trace -name "${sid}_*.trc" -or -name "${sid}_*.trm" $find_opts | xargs echo`
	files="$files $ORACLE_BASE/diag/rdbms/$db/$sid/trace/alert_$sid.log"
	tar_rotate $log_dir/traces.tar $files
	touch $ORACLE_BASE/diag/rdbms/$db/$sid/trace/alert_$sid.log

	# core dump files (aka cdump)
	files=`find $ORACLE_BASE/diag/rdbms/$db/$sid/cdump -name "${sid}_*.trc" -or -name "${sid}_*.trm" $find_opts | xargs echo`
	tar_rotate $log_dir/cdumps.tar $files

	# listener core dumps
	files=`find $ORACLE_BASE/diag/tnslsnr/*/listener/cdump -name "${sid}_*.trc" -or -name "${sid}_*.trm" $find_opts | xargs echo`
	tar_rotate $log_dir/cdumps.tar $files
	
	# client logs
	files=`find $ORACLE_HOME/log/*/client -name "clsc*.log" $find_opts | xargs echo`
	tar_rotate $log_dir/clients.tar $files
	
	# alert log
	files="$ORACLE_BASE/diag/rdbms/$db/$sid/alert/log.xml"
	tar_rotate $log_dir/alert.tar $files
	touch $files
	
	# startup & shutdown logs
	files="$ORACLE_HOME/startup.log $ORACLE_HOME/shutdown.log"
	tar_rotate $log_dir/startup_shutdown.tar $files
	touch $files
	
	# datapump log
	files="$ORACLE_HOME/rdbms/log/dp.log"
	tar_rotate $log_dir/dp.tar $files
	touch $files
done
