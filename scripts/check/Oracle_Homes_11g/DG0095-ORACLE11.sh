#!/bin/bash

. lib/oracle.sh

if [[ ("x$STIG_DB_CONFIDENTIALITY" = "xpublic" || "x$STIG_DB_CONFIDENTIALITY" = "xsensitive") && "x$STIG_DB_MAC" = "xadministrative" ]]; then
	notchecked "Audit trail data is not reviewed daily or more frequently"
fi

notapplicable
