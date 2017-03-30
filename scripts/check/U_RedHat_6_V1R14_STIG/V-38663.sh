#!/bin/bash

for file in `rpm -V audit | grep '^.M' | cut -c14-`; do
    pkg=`rpm -qf $file`
    rpm -q --queryformat "[%{FILENAMES} %{FILEMODES:perms}\n]" "$pkg" | grep "$file"
    ls -dlL "$file"
    echo
done
