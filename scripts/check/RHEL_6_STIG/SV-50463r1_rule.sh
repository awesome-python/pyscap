#!/bin/bash
. lib/general.sh

if [[ ! -s /etc/crypttab ]]; then
	fail "The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of data at rest unless otherwise protected by alternative physical measures: /etc/crypttab doesn't exist or has no entries"
fi

# mainline cryptoloop is not secure, so we don't test for it

if ! which dmsetup > /dev/null; then
	fail "The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of data at rest unless otherwise protected by alternative physical measures: dmsetup is not in PATH"
fi
if ! which cryptsetup > /dev/null; then
	fail "The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of data at rest unless otherwise protected by alternative physical measures: cryptsetup is not in PATH"
fi

if [[ "x$(dmsetup targets | grep crypt)" = "x" ]]; then
	fail "The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of data at rest unless otherwise protected by alternative physical measures: crypt device-mapper target doesn't exist"
fi

if [[ "$(dmsetup ls --target crypt | wc -l)" -le 0 ]]; then
	fail "The operating system must employ cryptographic mechanisms to prevent unauthorized disclosure of data at rest unless otherwise protected by alternative physical measures: no crypt devices found"
done

pass
