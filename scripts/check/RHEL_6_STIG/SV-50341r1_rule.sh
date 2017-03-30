#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'sethostname'
not_auditing_syscall_fail 'setdomainname'
not_auditing_file_fail '/etc/issue'
not_auditing_file_fail '/etc/issue.net'
not_auditing_file_fail '/etc/hosts'
not_auditing_file_fail '/etc/sysconfig/network'
echo '<result>pass</result>'
