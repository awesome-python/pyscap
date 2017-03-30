#!/usr/bin/perl
use strict;
use warnings;

if(! exists($ENV{'STIG_DATABASE'}))
{
print<<'EOF1';
	print_log("Enter the database type {mysql} [mysql]:");
	$ENV{'STIG_DATABASE'} = <STDIN>;
	chomp $ENV{'STIG_DATABASE'};
	if($ENV{'STIG_DATABASE'} eq '')
	{
		$ENV{'STIG_DATABASE'} = 'mysql';
	}
	print_log("\n");
	print_log("STIG_DATABASE = $ENV{'STIG_DATABASE'}\n");
EOF1
}

if(! exists($ENV{'STIG_DATABASE_USERNAME'}))
{
print<<'EOF2';
	print_log("Enter the database username [root]: ");
	$ENV{'STIG_DATABASE_USERNAME'} = <STDIN>;
	chomp $ENV{'STIG_DATABASE_USERNAME'};
	if($ENV{'STIG_DATABASE_USERNAME'} eq '')
	{
		$ENV{'STIG_DATABASE_USERNAME'} = 'root';
	}
	print_log("\n");
	print_log("STIG_DATABASE_USERNAME = $ENV{'STIG_DATABASE_USERNAME'}\n");
EOF2
}

if(! exists($ENV{'STIG_DATABASE_PASSWORD'}))
{
print<<'EOF3';
	print_log("Enter the database password: ");
	`stty -echo`;
	$ENV{'STIG_DATABASE_PASSWORD'} = <STDIN>;
	`stty echo`;
	chomp $ENV{'STIG_DATABASE_PASSWORD'};
	if($ENV{'STIG_DATABASE_PASSWORD'} eq '')
	{
		die "Unspecified database password";
	}
	print_log("\n");
EOF3
}
