#!/bin/bash

. lib/oracle.sh

f=/etc/audit/audit.rules
. lib/file.sh
backup_file $f || exit 1

r=`grep STIG_DB $f`
if [[ "x$r" != "x" ]]; then
	echo "AUDIT RULES ALREADY ADDED!!!"
	exit 1
fi

echo '# STIG_DB audits' >> $f
for i in bin $(cd $ORACLE_HOME; ls -d */admin/) rdbms/audit; do
	echo "-w $ORACLE_HOME/$i -p wa -k STIG_DB" >> $f
done

service auditd restart
sleep 5s