#!/bin/bash

. lib/oracle.sh

r=$(ps -ef | grep -i '(httpd|ftpd|postfix|qmgr|sendmail|catalina|jboss|WebSphere|zope|geronimo|glassfish|zend|jonas|mortbay)' | grep -v grep)
if [[ "x$r" != "x" ]]; then
	fail "The DBMS is operated without authorization on a host system supporting other application services: $r"
else
	pass
fi
