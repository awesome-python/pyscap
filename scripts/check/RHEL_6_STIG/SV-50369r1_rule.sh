#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'mount'
echo '<result>pass</result>'
