#!/bin/bash

r=`mount | grep cifs`
if [[ "x$r" == "x" ]]; then
	echo '<result>notapplicable</result>'
	exit
fi

r=`mount | grep cifs | grep '(sec=krb5i|sec=ntlmv2i)'`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result><message>CIFS mount does not use appropriate security</message>'
	exit
fi

echo '<result>pass</result>'