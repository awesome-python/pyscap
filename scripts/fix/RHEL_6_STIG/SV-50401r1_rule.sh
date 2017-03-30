#!/bin/bash

sh fix/RHEL_6_STIG/sysctl_key_value.sh 'net.ipv4.conf.default.send_redirects' 0 || exit 1