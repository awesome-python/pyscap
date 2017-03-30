#!/bin/bash

for d in /bin /usr/bin /usr/local/bin /sbin /usr/sbin /usr/local/sbin; do
    for f in `find -L "$d" -perm /022 -type f`; do
        ls -l "$f"
    done
done
