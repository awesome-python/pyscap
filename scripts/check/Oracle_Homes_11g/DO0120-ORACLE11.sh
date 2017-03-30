#!/bin/bash

. lib/oracle.sh

r=$(su -l oinstall -c 'groups' | grep root)
if [[ "x$r" != "x" ]]; then
	fail "The Oracle software installation account has been granted excessive host system privileges"
fi

pass
