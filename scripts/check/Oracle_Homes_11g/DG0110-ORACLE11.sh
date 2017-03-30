#!/bin/bash

. lib/oracle.sh

r=$(ps -ef | grep '(smbd|nmbd|winbindd|slapd|ldap|kdc|kadmind|kerberos|ypserv|ypbind|ndsd|pwcheck|saslauthd|apache\.directory\.server|oidmon|lotus)' | grep -v grep)
if [[ "x$r" != "x" ]]; then
	fail "The DBMS shares a host supporting an independent security service: $r"
else
	pass
fi
