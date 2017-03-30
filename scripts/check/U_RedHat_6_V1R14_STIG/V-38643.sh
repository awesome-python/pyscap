#!/bin/bash

for p in `mount -t xfs,ext4,ext3,ext2,ext | cut -f3 -d' '`; do
    for f in `find "$p" -xdev -type f -perm -002 2>/dev/null`; do
        if [[ $(grep "$f" /etc/audit/audit.rules 2>/dev/null) ]]; then
            echo "$f has entries"
        else
            echo "$f does NOT have entries"
        fi
    done
done
