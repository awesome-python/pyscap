#!/bin/bash

rpm -Va 2>/dev/null | grep '^.M' | awk '{print $3}' | perl -e '
while(<>)
{
	chomp;
	#print "File: $_\n";
	next if ! -f $_;
	my $pkg = `rpm -qf $_`; 
	chomp $pkg;
	#print "Package: $pkg\n";
	my $rpm_mode = `rpm -q --queryformat "[%{FILENAMES} %{FILEMODES}\n]" $pkg | grep "$_"`;
	chomp $rpm_mode;
	$rpm_mode =~ s/\S*\s+(\S*)$/$1/;
	$rpm_mode &= 07777;
	#printf "%04o\n", $rpm_mode;
	my $mode = ((stat($_))[2]) & 07777;
	#printf "%04o\n", $mode;
	if($mode != $rpm_mode)
	{
		printf "<result>fail</result><message>Mode of file %s, %04o does not match package, %04o</message>\n", $_, $mode, $rpm_mode;
		exit;
	}
}
print "<result>pass</result>\n";
'
