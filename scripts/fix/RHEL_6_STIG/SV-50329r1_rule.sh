#!/bin/bash

sh fix/RHEL_6_STIG/sysctl_key_value.sh net.ipv4.conf.all.log_martians 1 || exit 1
