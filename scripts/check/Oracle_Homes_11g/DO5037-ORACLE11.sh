#!/bin/bash

. lib/oracle.sh
. lib/file.sh

# Oracle SQLNet and listener log files are accessible to unauthorized users

f=$ORACLE_HOME/network/admin/sqlnet.ora
if [[ -f $f ]]; then
	r=$(grep TRACE_LEVEL_SERVER $f)
	if [[ "x$r" != "x" ]]; then
		 r=$(echo $r | sed 's/^TRACE_LEVEL_SERVER\s*=\s*//')
		 if [[ ! $r =~ OFF && "$r" != 0 ]]; then
			dir=$(grep LOG_DIRECTORY_SERVER $f | sed 's/^LOG_DIRECTORY_SERVER\s*=\s*//')
			file=$(grep LOG_FILE_SERVER $f | sed 's/^LOG_FILE_SERVER\s*=\s*//')
			if [[ -d $dir ]]; then
				# check log file
				fail_if_world_readable $dir
				fail_if_world_readable $dir/$file
				
				# check trace files
				dir=$(echo $file | sed 's/\/log/\/trace/')
				file=$(echo $file | sed 's/\.log$/.trc/')
				fail_if_world_readable $dir
				fail_if_world_readable $dir/$file
			else
				# otherwise check default locations
				fail_if_world_readable $ORACLE_HOME/network/log/sqlnet.log
				fail_if_world_readable $ORACLE_HOME/network/trace/sqlnet.trc
			fi
		 fi
	fi
fi

f=$ORACLE_HOME/network/admin/listener.ora
for i in $(oracle_listeners); do
	if [[ "x$(grep -i 'DIAG_ADR_ENABLED_$i\s*=\s*ON' $f)" != "x" ]]; then
		# adr is on
		notchecked "Oracle SQLNet and listener log files are accessible to unauthorized users: ADR is on"
	else	# off by default
		# check log file
		dir=$(grep LOG_DIRECTORY_$i $f | sed "s/^LOG_DIRECTORY_$i\s*=\s*//")
		file=$(grep LOG_FILE_$i $f | sed "s/^LOG_FILE_$i\s*=\s*//")
		if [[ -d $dir ]]; then
			fail_if_world_readable $dir
			fail_if_world_readable $dir/$file
		else
			# otherwise check default locations
			fail_if_world_readable $ORACLE_HOME/network/log
			fail_if_world_readable $ORACLE_HOME/network/log/listener.log
		fi
		
		# check
		tdir=$(grep TRACE_DIRECTORY_$i $f | sed "s/^TRACE_DIRECTORY_$i\s*=\s*//")
		if [[ -d $tdir ]]; then
			fail_if_world_readable $tdir
			file=$(echo $file | sed 's/\.log$/.trc/')
			fail_if_world_readable $tdir/$file
		else
			# otherwise check default locations
			fail_if_world_readable $ORACLE_HOME/network/trace
			fail_if_world_readable $ORACLE_HOME/network/trace/listener.trc
		fi
	fi
done

pass
