#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'clock_settime'
echo '<result>pass</result>'



