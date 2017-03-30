#!/bin/bash

sh fix/RHEL_6_STIG/sysctl_key_value.sh 'net.ipv4.conf.all.rp_filter' 1 || exit 1