#!/bin/bash
. lib/oracle.sh
. lib/file.sh

die_if_no_ORACLE_HOME
# check installation
which aide >/dev/null 2>/dev/null
if [[ "$?" != 0 ]]; then
	echo Installing aide...
	echo 'y' | yum install aide
	if [[ "$?" != 0 ]]; then
		die "aide installation failed"
	fi

	# just basic config
	mv /etc/aide.conf /etc/aide.conf.orig 2>/dev/null
	f=/etc/aide.conf
	cat >> $f << EOF_AIDE
@@define DBDIR /var/lib/aide
@@define LOGDIR /var/log/aide
database=file:@@{DBDIR}/aide.db.gz
database_out=file:@@{DBDIR}/aide.db.new.gz
gzip_dbout=yes
verbose=5
report_url=file:@@{LOGDIR}/aide.log
report_url=stdout

ALLXTRAHASHES = sha1+rmd160+sha256+sha512+tiger
EVERYTHING = R+ALLXTRAHASHES
NORMAL = R+rmd160+sha256
DIR = p+i+n+u+g+acl+selinux+xattrs
PERMS = p+i+u+g+acl+selinux
LOG = >
LSPP = R+sha256
DATAONLY =  p+n+u+g+s+acl+selinux+xattrs+md5+sha256+rmd160+tiger

/etc/aide.conf NORMAL

EOF_AIDE

	aide --init
	if [[ "$?" != "0" ]]; then
		die "aide initialization failed"
	fi
	
	mv -f /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

	echo "Installation successful."
else
	echo "AIDE already installed."
fi

# check policy
f=/etc/aide.conf
backup_file $f
if [[ "x$(grep STIG_DB_AIDE $f 2>/dev/null)" == "x" ]]; then
	cat >> $f << EOF_STIG_DB_AIDE
# STIG_DB_AIDE
# Additions for Oracle binaries and config
# binaries
$ORACLE_HOME/bin			NORMAL
$ORACLE_HOME/lib			NORMAL

# config
/etc/oratab					NORMAL
$ORACLE_HOME/network/admin	NORMAL
EOF_STIG_DB_AIDE
	if [[ "$?" != "0" ]]; then
		die "AIDE policy installation failed"
	fi
	
	aide --update # returns 1 for new files added
	if [[ "$?" != "1" ]]; then
		die "AIDE policy update failed"
	fi
	
	mv -f /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

	echo "AIDE policy installation successful."
else
	echo "Oracle AIDE policy already added"
fi


