#!/bin/bash

. lib/audit.sh

not_auditing_syscall_fail 'chmod'
echo '<result>pass</result>'
