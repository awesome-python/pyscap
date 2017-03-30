#!/bin/bash

# Access to external executables must be disabled or restricted.

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/mysql.sh
	# there's no way to ensure that plugins won't provide this functionality, so we check that plugins are in an allowed list

	u=''
	r=`mysql_query 'SHOW PLUGINS;' | cut -f1`
	for i in $r; do
		case $i in
			# add approved plugins below
			binlog) ;;
			partition) ;;
			CSV) ;;
			MEMORY) ;;
			InnoDB) ;;
			MyISAM) ;;
			MRG_MYISAM) ;;
			authentication_pam) ;;
			audit_log) ;;
			mysql_native_password) ;;
			mysql_old_password) ;;
			sha256_password) ;;
			FEDERATED) ;;
			INNODB_TRX) ;;
			INNODB_LOCKS) ;;
			INNODB_LOCK_WAITS) ;;
			INNODB_CMP) ;;
			INNODB_CMP_RESET) ;;
			INNODB_CMPMEM) ;;
			INNODB_CMPMEM_RESET) ;;
			INNODB_CMP_PER_INDEX) ;;
			INNODB_CMP_PER_INDEX_RESET) ;;
			INNODB_BUFFER_PAGE) ;;
			INNODB_BUFFER_PAGE_LRU) ;;
			INNODB_BUFFER_POOL_STATS) ;;
			INNODB_METRICS) ;;
			INNODB_FT_DEFAULT_STOPWORD) ;;
			INNODB_FT_DELETED) ;;
			INNODB_FT_BEING_DELETED) ;;
			INNODB_FT_CONFIG) ;;
			INNODB_FT_INDEX_CACHE) ;;
			INNODB_FT_INDEX_TABLE) ;;
			INNODB_SYS_TABLES) ;;
			INNODB_SYS_TABLESTATS) ;;
			INNODB_SYS_INDEXES) ;;
			INNODB_SYS_COLUMNS) ;;
			INNODB_SYS_FIELDS) ;;
			INNODB_SYS_FOREIGN) ;;
			INNODB_SYS_FOREIGN_COLS) ;;
			INNODB_SYS_TABLESPACES) ;;
			INNODB_SYS_DATAFILES) ;;
			ARCHIVE) ;;
			BLACKHOLE) ;;
			PERFORMANCE_SCHEMA) ;;
			*)
				u="$u $i"
				;;
		esac
	done
	
	if [[ ! -z "$u" ]]; then
		fail "Unknown plugin(s): $u"
	fi

	pass
else
	notchecked
fi
