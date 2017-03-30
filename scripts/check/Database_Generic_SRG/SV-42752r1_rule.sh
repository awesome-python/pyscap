#!/bin/bash

. lib/db.sh
error_if_no_db
. lib/audit.sh

if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	# check mysql executables
	for g in mysql mysqlaccess mysqladmin mysqlbinlog mysqlbug mysqlcheck mysql_config mysql_convert_table_format mysqld_multi mysqld_safe mysqldump mysqldumpslow mysql_find_rows mysql_fix_extensions mysql_fix_privilege_tables mysqlhotcopy mysqlimport mysql_install_db mysql_secure_installation mysql_setpermission mysqlshow mysqlslap mysqltest mysql_tzinfo_to_sql mysql_upgrade mysql_waitpid mysql_zap; do
		f=`which $g 2>/dev/null`
		if [[ $? == 0 && -f $f ]]; then
			not_auditing_file_fail "$f"
		fi
		# else file doesn't exist or wasn't found in the path, so we skip it
	done
	# check the "real" executables not in the path
	for f in /usr/libexec/mysql /usr/libexec/mysqlmanager; do
		if [[ -f $f ]]; then
			not_auditing_file_fail "$f"
		fi
	done
	
	# might be more config files we should be checking, but these are the important ones
	for f in /etc/my.cnf /etc/mysql/my.cnf; do
		if [[ -f $f ]]; then
			not_auditing_file_fail "$f"
		fi
	done
	pass
else
	notchecked
fi
