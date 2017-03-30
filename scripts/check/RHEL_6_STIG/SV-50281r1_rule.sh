#!/bin/bash

. lib/general.sh

yum check-update 2>/dev/null 1>/dev/null
if [[ "$?" != "0" ]]; then
	fail "System security patches and updates must be installed and up-to-date. Packages last updates:
$(rpm -qa -last)"
fi

pass