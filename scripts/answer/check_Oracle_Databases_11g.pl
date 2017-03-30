#!/usr/bin/perl
use strict;
use warnings;

if(! exists($ENV{'ORACLE_HOME'}))
{
print<<'EOF1';
	print_log("Enter the Oracle home path [/opt/oracle/product/11.2.0/db]:");
	$ENV{'ORACLE_HOME'} = <STDIN>;
	chomp $ENV{'ORACLE_HOME'};
	if($ENV{'ORACLE_HOME'} eq '')
	{
		$ENV{'ORACLE_HOME'} = '/opt/oracle/product/11.2.0/db';
	}
	$ENV{'PATH'} = $ENV{'PATH'} . ':' . $ENV{'ORACLE_HOME'} . '/bin';
	print_log("\n");
	print_log("ORACLE_HOME = $ENV{'ORACLE_HOME'}\n");
	print_log("PATH = $ENV{'PATH'}\n");
EOF1
}
