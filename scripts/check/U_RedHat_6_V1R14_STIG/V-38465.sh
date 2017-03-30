#!/bin/bash

for dir in /lib /lib64 /usr/lib /usr/lib64; do
    for file in `find -L "$dir" -perm /022 -type f`; do
        ls -l "$file"
    done
done
