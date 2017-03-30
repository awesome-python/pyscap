#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'chown'
echo '<result>pass</result>'
