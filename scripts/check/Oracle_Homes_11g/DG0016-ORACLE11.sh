#!/bin/bash

. lib/oracle.sh

fail_if_no_ORACLE_HOME
q=`oracle_packages`
for i in $q; do
	case $i in
		Oracle\ Active\ Data\ Guard|Oracle\ Total\ Recall|Oracle\ Real\ Application\ Clusters|Oracle\ In-Memory\ Database\ Cache|Oracle\ Advanced\ Security|Oracle\ Label\ Security|Oracle\ Database\ Vault|Oracle\ Change\ Management\ Pack|Oracle\ Configuration\ Management\ Pack|Oracle\ Diagnostic\ Pack|Oracle\ Tuning\ Pack|Oracle\ Provisioning\ and\ Patch\ Automation\ Pack|Oracle\ Real\ Application\ Testing|Oracle\ Partitioning|Oracle\ OLAP|Oracle\ Data\ Mining|Oracle\ Data\ Quality\ and\ Profiling|Oracle\ Data\ Watch\ and\ Repair\ Connector|Oracle\ Advanced\ Compression|Oracle\ Spatial|Oracle\ Content\ Database\ Suite|Oracle\ Database\ Gateways|Database\ Workspace\ Manager|Enterprise\ Manager\ Agent|iSQL\*Plus|LDAP|Oracle\ Data\ Guard|Oracle\ Fail\ Safe|Oracle\ HTTP\ Server|Oracle\ interMedia|Oracle\ Internet\ Directory|Oracle\ Advanced\ Replication|Oracle\ Starter\ Database|Oracle\ Text|Oracle\ Virtual\ Private\ Database|Oracle\ Wallet\ Manager|Oracle\ XML\ Development|Sample\ Schema)
			
			fail "Unused database components, database application software or database objects have not been removed from the DBMS system: $q"
			;;
		*)
			;;
	esac
done
pass
