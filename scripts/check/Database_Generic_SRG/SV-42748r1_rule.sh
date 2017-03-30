#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	. lib/file.sh
	
	if [[ -f /usr/libexec/mysqld ]]; then
		real_mysqld=/usr/libexec/mysqld
	elif [[ -f /usr/sbin/mysqld ]]; then
		real_mysqld=/usr/sbin/mysqld
	elif [[ -f /usr/bin/mysqld ]]; then
		real_mysqld=/usr/sbin/mysqld
	else
		echo '<result>error</result><message>Could not determine where the real mysqld executable is located</message>'
		exit
	fi
	
	#echo $real_mysqld
	
	for l in `ldd $real_mysqld | perl -e '
while(<>)
{
	chomp;
	my @bits = split /\s/;
	if ($bits[1] =~ m|^/|)
	{
		print "$bits[1]\n";		# absolute path linked in, no resolution necessary
	}
	elsif($bits[3] !~ /^\s*$/)	# skip unresolved libraries
	{
		print "$bits[3]\n";		# relative path, so return the resolved path
	}
}
'`; do
		mode=`file_mode $l`
		owner=`file_owner $l`
		gowner=`file_groupowner $l`
		#echo "$l mode: $mode owner: $owner gowner: $gowner"
		if [[ "$(file_perm_gt $mode '0755')" = "true" ]] ; then
			echo "<result>fail</result><message>$l mode $mode is greater than 0755</message>"
			exit
		fi
		if [[ "x$owner" != "xroot" ]]; then
			echo "<result>fail</result><message>$l owner $owner is not root</message>"
			exit
		fi
		if [[ "x$gowner" != "xroot" ]]; then
			echo "<result>fail</result><message>$l owner $gowner is not root</message>"
			exit
		fi
	done
	echo '<result>pass</result>'
else
	echo '<result>notchecked</result>'
fi