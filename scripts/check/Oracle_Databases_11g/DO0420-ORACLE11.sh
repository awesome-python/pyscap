#!/bin/bash

. lib/oracle.sh

e=$(sqlplus_sysdba "select count(*) from dba_users where username = 'XDB';")
if [[ $e =~ ^\s*0\s*$ ]]; then
	pass
fi

e=$(sqlplus_sysdba "select count(*) from v\$parameter where name = 'dispatchers'
and value like '%XDB%';")
if [[ $e =~ ^\s*0\s*$ ]]; then
	pass
fi

fail "The XDB Protocol server is installed and not required and authorized for use."