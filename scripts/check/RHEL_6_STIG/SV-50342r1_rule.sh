#!/bin/bash

. lib/audit.sh
not_auditing_dir_fail '/etc/selinux'
echo '<result>pass</result>'
