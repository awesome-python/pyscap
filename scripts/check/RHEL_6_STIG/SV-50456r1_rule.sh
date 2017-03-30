#!/bin/bash
. lib/general.sh

if [[ "x$(grep noexec /etc/fstab)" = "x" ]]; then
	fail "The noexec option must be added to removable media partitions: /etc/fstab doesn't contain noexec"
fi

pass