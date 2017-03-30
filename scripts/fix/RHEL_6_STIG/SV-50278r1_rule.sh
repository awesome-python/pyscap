#!/bin/bash

r=`grep CentOS /etc/redhat-release`
if [[ "x$r" == "x" ]]; then
	chkconfig rhnsd off
	service rhnsd stop
	sleep 5
fi
