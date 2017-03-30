#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME

su -l oracle -c 'tnsping localhost' > /dev/null
if [[ $? == 0 ]]; then
	t="running"
else
	t="not running"
fi

f=$ORACLE_HOME/network/admin/cman.ora
if [[ -f $f ]]; then
	r=$(grep -Pizo '\(CONFIGURATION' $f)
	if [[ "x$r" == "x" ]]; then
		c="not configured"
	else
		c="configured"
	fi
else
	c="not configured"
fi

# If Oracle Listener, JAVA Listener, Oracle Names and Connection Manager are not running on the local database host server, this check is Not a Finding.
if [[ "x$t" = "xnot running" && "x$c" = "xnot configured" ]]; then
	notapplicable
fi

# Review the listener.ora file located by default in the ORACLE_HOME\network\admin directory or
# in the directory specified in the environment variable TNS_ADMIN defined for the listener process
# or service.
# View the "PORT=" parameter for any protocols defined.
# If any do not match an entry in the following list, then confirm that it is not a default or registered
# port for the service.
f=$ORACLE_HOME/network/admin/listener.ora
r=$(grep -Pizo 'PORT\s*=\s*[0-9]+' $f | wc -l)
if [[ "$r" -gt "0" ]]; then
	p=$(grep -Pizo 'PORT\s*=\s*(1521|2483|2484|2481|2482|1575|1830)' $f | wc -l)
	if [[ "$r" -ne "$p" ]]; then
		fail "DBMS network communications do not comply with PPS usage restrictions: $r != $p"
	fi
fi

# View the cman.ora file in the ORACLE_HOME/network/admin directory.
# If the file does not exist, the database is not accessed via Oracle Connection Manager and this
# part of the check is Not a Finding.
# View the "PORT=" parameter for any protocols defined.
# If any do not match an entry in the following list, then confirm that it is not a default or registered
# port for the service.
f=$ORACLE_HOME/network/admin/cman.ora
if [[ -f $f ]]; then
	r=$(grep -Pizo 'PORT\s*=\s*[0-9]+' $f | wc -l)
	if [[ "$r" -gt "0" ]]; then
		p=$(grep -Pizo 'PORT\s*=\s*(1521|2483|2484|2481|2482|1575|1830)' $f | wc -l)
		if [[ "$r" -ne "$p" ]]; then
			fail "DBMS network communications do not comply with PPS usage restrictions: $r != $p"
		fi
	fi
fi

# If any non-default or non-registered ports are listed, this is a Finding.
# Default Oracle Listener Ports: 1521, 2483, 2484
# Default Java Listener Ports: 2481, 2482
# Default Oracle Names Listener Port: 1575
# Default Connection Manager Ports: 1521, 1830
# Registered ports MAY be listed at http://www.iana.org/assignments/port-numbers or in the DoD
# Ports, Protocols, and Services Category Assurance List (CAL).
pass
