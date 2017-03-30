#!/bin/bash
# for each line in /etc/rsyslog.conf /etc/rsyslog.d/*
    # if starts with $, ignore
    # if starts with #, ignore
    # split selectors from destination
    # strip off leading -
    # if destination == *, ignore
for f in /dev/console /var/log/messages /var/log/secure /var/log/maillog /var/log/cron /var/log/spooler /var/log/boot.log; do
    ls -l "$f"
    # if owner not root, fail
done

# pass
