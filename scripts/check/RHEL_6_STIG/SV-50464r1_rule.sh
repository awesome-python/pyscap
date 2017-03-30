#!/bin/bash

rpm -V audit 2>/dev/null | grep '^.M' | awk '{print $3}' | perl -e '
while(<>)
{
	chomp;
	#print "$_\n";
	my $rpm_mode = `rpm -q --queryformat "[%{FILENAMES} %{FILEMODES}\n]" audit | grep "$_"`;
	chomp $rpm_mode;
	$rpm_mode =~ s/\S*\s+(\S*)$/$1/;
	$rpm_mode &= 07777;
	#printf "%04o\n", $rpm_mode;
	my $mode = ((stat($_))[2]) & 07777;
	#printf "%04o\n", $mode;
	if($mode != $rpm_mode)
	{
		printf "<result>fail</result><message>File mode of $_ is %04o, should be %04o</message>\n", $mode, $rpm_mode;
		exit;
	}
}
print "<result>pass</result>\n";
'