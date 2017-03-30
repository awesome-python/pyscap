#!/bin/bash

e=`sysctl kernel.randomize_va_space | grep -P 'kernel\.randomize_va_space\s*=\s*[1|2]$'`
if [[ "x$e" == "x" ]]; then
	echo '<result>fail</result><message>kernel.randomize_va_space is not 1 or 2</message>'
	exit
fi

echo '<result>pass</result>'
