#!/bin/bash

. lib/audit.sh
not_auditing_file_fail '/etc/sudoers'
echo '<result>pass</result>'
