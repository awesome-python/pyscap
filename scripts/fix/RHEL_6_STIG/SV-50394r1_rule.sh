#!/bin/bash

f=/etc/issue
. lib/file.sh
backup_file "$f" || exit 1

cat lib/DoD_banner.txt > $f