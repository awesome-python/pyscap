#!/bin/bash

. lib/audit.sh

not_auditing_file_fail "/etc/localtime"
echo '<result>pass</result>'
