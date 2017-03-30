#!/bin/bash

sh fix/RHEL_6_STIG/sysctl_key_value.sh net.ipv6.conf.default.accept_redirects 0 || exit 1