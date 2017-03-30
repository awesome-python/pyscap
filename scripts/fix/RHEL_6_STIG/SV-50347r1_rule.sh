#!/bin/bash
. lib/general.sh
. lib/file.sh

echo "TODO this doesn't remove the ipv6 mod from the running kernel, so a reboot is necessary to apply"
echo 'options ipv6 disable=1' >> /etc/modprobe.d/STIG.conf

if [[ "x$(alternatives --display mta | grep 'link currently' | grep 'sendmail.postfix')" != "x" ]]; then
	echo "Using postfix, removing ipv6 from config..."
	f=/etc/postfix/main.cf
	backup_file $f
	if [[ "x$(grep '^inet_protocols' $f)" == "x" ]]; then
		echo 'inet_protocols = ipv4' >> $f
	else
		sed 's/^inet_protocols\s*=.*$/inet_protocols = ipv4/' $f.new
		mv -f $f.new $f
	fi
fi
