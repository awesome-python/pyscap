#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME
q=`find $ORACLE_HOME /var/opt/oracle /etc/ora* /usr/local/bin/*ora* /usr/local/bin/db* ! -user oracle -o ! \( -group dba -o -group oinstall \) | xargs ls -lR -d`
if [[ "x$q" != "x" ]]; then
	fail "Application software is not owned by a Software Application account:
$q"
fi

bins=""
for i in extjob jssu nmb nmhs nmo oradism externaljob.ora coraenv dbhome oraenv; do
	j=$(su -l oracle -c "which $i" 2>/dev/null)
	echo "which $i = $j"
	if [[ $j =~ ^/ ]]; then
		bins="$bins $j"
	fi
done

q=`find $bins ! -user oracle -o ! -group dba | xargs ls -lR -d`
if [[ "x$q" != "x" ]]; then
	fail "Application software is not owned by a Software Application account: $q"
fi

pass
