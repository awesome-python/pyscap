#!/bin/bash

r=`grep CentOS /etc/redhat-release`
if [[ "x$r" == "x" ]]; then
	rhn_register
else
	echo "Running CentOS...no rhn_register"
	exit 1
fi
