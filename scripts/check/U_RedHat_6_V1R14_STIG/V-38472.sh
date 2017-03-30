#!/bin/bash

for d in /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin; do
    find -L "$d" \! -user root
done
