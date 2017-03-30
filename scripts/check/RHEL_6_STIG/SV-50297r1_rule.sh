#!/bin/bash

. lib/general.sh

r=$(sed -n '/^\(root:\|[^:]\+:[*!]\)/! p' /etc/shadow | cut -d: -f1)
fail "Default system accounts, other than root, must be locked. Unlocked non-root accounts:
$r"