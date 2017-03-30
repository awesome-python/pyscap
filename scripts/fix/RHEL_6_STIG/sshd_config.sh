#!/bin/bash

f=/etc/ssh/sshd_config
. lib/file.sh
backup_file "$f" || exit 1

r=`grep STIG_RHEL_6 $f`
if [[ "x$r" != "x" ]]; then
	echo "sshd_config fixes already applied!!!"
	exit 1
fi

function fix_var() {
	# Usage fix_var name value
	r=`egrep -i "^$1" $f`
	if [[ "x$r" == "x" ]]; then
		echo "$1 $2" >> $f
	else
		r=$(echo $2 | sed 's/\//\\\//g')
		sed "s/^$1.*$/$1 $r/gI" $f >> $f.new
		if [[ "$?" != "0" ]]; then
			echo "Couldn't replace param $1 with value $2"
			rm $f.new
			exit
		fi
		mv -f $f.new $f
	fi
	return 0
}

echo '' >> $f
echo "# STIG_RHEL_6 additions" >> $f

fix_var 'Protocol' '2'
fix_var 'PrintLastLog' 'yes'
fix_var 'ClientAliveInterval' '900'
fix_var 'ClientAliveCountMax' '0'
fix_var 'Ciphers' 'aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc'
fix_var 'PermitUserEnvironment' 'no'
fix_var 'Banner' '/etc/issue'
fix_var 'PermitRootLogin' 'no'

service sshd restart
sleep 5s
