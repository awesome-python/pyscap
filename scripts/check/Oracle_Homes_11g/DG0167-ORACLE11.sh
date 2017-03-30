#!/bin/bash

. lib/oracle.sh

error_if_no_ORACLE_HOME

if [[ ! $STIG_DB_CONFIDENTIALITY =~ public ]]; then
	notapplicable "Sensitive data served by the DBMS is not protected by encryption when transmitted across the network"
fi

f=$ORACLE_HOME/network/admin/listener.ora
r=$(grep -Pizo 'PROTOCOL\s*=\s*(IPC|NMP|TCP|TCPS)' $f 2>/dev/null | wc -l)
p=$(grep -Pizo 'PROTOCOL\s*=\s*(IPC|TCPS)' $f 2>/dev/null | wc -l)
if [[ "$r" -ne "$p" ]]; then
	fail "Sensitive data served by the DBMS is not protected by encryption when transmitted across the network: listener PROTOCOL is not TCPS: $r != $p"
fi

pass
