#!/bin/bash

. lib/oracle.sh

which aide >/dev/null 2>/dev/null
if [[ "$?" != 0 ]]; then
	fail "Database executable and configuration files are not being monitored for unauthorized modifications: aide is not installed"
fi

if [[ "x$(aide --check | grep STIG_DB_TRIPWIRE)" == "x" ]]; then
	fail "Database executable and configuration files are not being monitored for unauthorized modifications: aide policies for Oracle are not installed"
fi

pass