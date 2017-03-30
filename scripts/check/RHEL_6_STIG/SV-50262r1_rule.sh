#!/bin/bash

r=`grep nosignature /etc/rpmrc /usr/lib/rpm/rpmrc /usr/lib/rpm/redhat/rpmrc ~root/.rpmrc 2>/dev/null`
if [[ "x$r" != "x" ]]; then
	echo '<result>fail</result><message>nosignature found in rpmrc file</message>'
	exit
fi

echo '<result>pass</result>'