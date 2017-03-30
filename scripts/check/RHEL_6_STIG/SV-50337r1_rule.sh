#!/bin/bash

. lib/audit.sh

not_auditing_file_fail '/etc/passwd'
not_auditing_file_fail '/etc/shadow'
not_auditing_file_fail '/etc/group'
not_auditing_file_fail '/etc/gshadow'
not_auditing_file_fail '/etc/security/opasswd'
echo '<result>pass</result>'
