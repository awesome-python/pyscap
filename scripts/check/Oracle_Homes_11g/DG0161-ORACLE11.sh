#!/bin/bash

. lib/oracle.sh

if [[ $STIG_DB_CONFIDENTIALITY =~ (sensitive|public) && $STIG_DB_MAC =~ administrative ]]; then
	notapplicable "An automated tool that monitors audit data and immediately reports suspicious activity is not employed for the DBMS"
fi

r=$(sqlplus_sysdba "SELECT COUNT(*) FROM AUD\$;")
if [[ "$r" -gt 0 ]]; then
	fail "An automated tool that monitors audit data and immediately reports suspicious activity is not employed for the DBMS"
fi

pass
