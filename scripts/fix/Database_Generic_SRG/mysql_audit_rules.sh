#!/bin/bash

# this is the audit.rules super fix for mysql

f=/etc/audit/audit.rules
. lib/file.sh
backup_file $f || exit 1

r=`grep STIG_DB $f`
if [[ "x$r" != "x" ]]; then
	echo "DB AUDIT RULES ALREADY ADDED!!!"
	exit 1
fi

uname_i=`uname -i`

if [[ $uname_i == "x86_64" ]]; then
	archs="b32 b64"
else
	archs='b32'
fi

add_rule() {
	echo $1 >> $f
}

add_rule ''
add_rule '# STIG_DB database file rules'
for i in {columns_priv,db,event,func,host,plugin,proc,procs_priv,proxies_priv,servers,tables_priv,user}.{frm,MYD,MYI}; do
	if [[ ! -f "/var/lib/mysql/mysql/$i" ]]; then
		continue
	fi
	add_rule "-w /var/lib/mysql/mysql/$i -p wa -k audit_db_file"
done

for f in /etc/my.cnf /etc/mysql/my.cnf; do
	if [[ -f $f ]]; then
		add_rule "-w $f -p wa -k audit_db_file"
	fi
done

add_rule ''
add_rule '# STIG_DB database bin rules'
for i in `ls /usr/bin/myisam* /usr/bin/mysql* /usr/sbin/mysql*`; do
	add_rule "-w $i -p wa -k audit_db_bin"
done

add_rule ''
add_rule '# STIG_DB database lib rules'
if [[ $uname_i == "x86_64" ]]; then
	mydir="/usr/lib64/mysql"
else
        mydir='/usr/lib/mysql'
fi
for i in `ls $mydir/*.so $mydir/plugin/*.so`; do
	add_rule "-w $i -p wa -k audit_db_lib"
done

service auditd restart
sleep 5s
