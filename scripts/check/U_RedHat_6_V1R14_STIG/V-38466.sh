#!/bin/bash

for i in /lib /lib64 /usr/lib /usr/lib64 /usr/local/lib /usr/local/lib64; do
    for j in `find -L $i \! -user root`; do
        rpm -V -f $j | grep '^.....U'
    done 
done
