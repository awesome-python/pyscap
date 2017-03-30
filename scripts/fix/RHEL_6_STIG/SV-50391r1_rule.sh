#!/bin/bash

r=`rpm -q screen | grep 'not installed'`
if [[ "x$r" != "x" ]]; then
	echo 'y' | yum install screen
fi
