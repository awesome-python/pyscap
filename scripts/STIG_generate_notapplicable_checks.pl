#!/usr/bin/perl -w
use strict;
use XML::Parser;

sub usage
{
	print STDERR "Usage: $0 benchmark.xml [--parse-only] [--debug]\n";
}

if(scalar(@ARGV) < 1)
{
	usage();
	exit 1;
}

my $xmlfile = shift @ARGV;
my $parse_only = 0;
my $debug = 0;

foreach my $arg(@ARGV)
{
	if($arg =~ /--parse-only/)
	{
		$parse_only = 1;
	}
	elsif($arg =~ /--debug/)
	{
		$debug = 1;
	}
}

$::Benchmark_id = undef;
%::rules = ();
$::cur_rule = undef;
$::in_version = 0;

sub xml_handle_start
{
	my( $expat, $element, %attrs ) = @_;
	
	if($element =~ /^.*[:]?Benchmark$/)
	{
		$::Benchmark_id = $attrs{'id'};
	}
	elsif($element =~ /^.*[:]?Rule$/)
	{
		$::cur_rule = $attrs{'id'};
	}
	elsif($element =~ /^.*[:]?version$/ && defined($::cur_rule))
	{
		$::in_version = 1;
	}
}

sub xml_handle_end
{
    my( $expat, $element ) = @_;
	
	if($element =~ /^.*[:]?Rule$/)
	{
		$::cur_rule = undef;
	}
	elsif($element =~ /^.*[:]?version$/ && defined($::cur_rule))
	{
		$::in_version = 0;
	}
}

sub xml_handle_char
{
    my( $expat, $string ) = @_;
	if(defined($::cur_rule) && $::in_version)
	{
		$::rules{$::cur_rule}{'version'} = $string;
	}
}


my $parser = XML::Parser->new(
	ErrorContext => 2,
	Handlers =>
	{
		  Start=>\&xml_handle_start,
		  End=>\&xml_handle_end,
		  Char=>\&xml_handle_char,
	}
);
eval { $parser->parsefile( $xmlfile ); };

# report any error that stopped parsing
if( $@ ) {
    $@ =~ s/at \/.*?$//s;               # remove module line number
    print STDERR "\nERROR in '$xmlfile':\n$@\n";
	exit 1;
}

if($parse_only)
{
	print STDERR "Parsing completed successfully\n";
	print STDERR scalar(keys(%::rules)), " rules loaded\n";
	exit;
}

# run tests
RULE: foreach(sort keys(%::rules))
{
	my ($check_script, $check_cmd);
	if($^O eq 'linux')
	{
		$check_script = "check/$_.sh";
		$check_cmd = "sh $check_script";
	}
	#elsif($^O eq 'MSWin32')
	#{
	#	$check_script = "check/$_.bat";
	#	$check_cmd = "$check_script";
	#}
	else
	{
		print STDERR "Unsupported operating system $^O\n";
	}
	
	print STDERR "Checking rule $_...";
	if(-f $check_script)
	{
		print STDERR "Skipping existing rule.\n";
		next RULE;
	}
	else
	{
		if($::rules{$_}{'version'} =~ /-NA$/)
		{
			print STDERR "not applicable, making dummy check\n";
			open FH, '>', $check_script or die "Couldn't open $check_script";
			print FH "#!/bin/bash

echo 'notapplicable'
";
			close FH or die "Couldn't close $check_script";
		}
		else
		{
			print STDERR "applicable.\n";
		}
	}
}