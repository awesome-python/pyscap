#!/usr/bin/perl -w
use strict;

sub usage {
	print STDERR "Usage: $0 'line_to_insert' \{before|after\} [!] 'pattern'\n";
	exit 1;
}

if(! defined($ARGV[0])
	|| ! defined($ARGV[1])
	|| ! defined($ARGV[2])
	|| $ARGV[0] eq ''
	|| $ARGV[1] !~ /^(after|before)$/
	|| $ARGV[2] eq '')
{
	usage();
}

my $text = $ARGV[0];
$text =~ s/\\n/\n/gm;
$text =~ s/\\t/\t/gm;
my $pos = $ARGV[1];
my $negate_pat = 0;
my $pat = '';

if($ARGV[2] eq '!')
{
	$negate_pat = 1;
	#print STDERR "*** Negating pattern\n";
	if(! defined($ARGV[3]) || $ARGV[3] eq '')
	{
		usage();
	}
	
	$pat = $ARGV[3];
}
else
{
	$pat = $ARGV[2];
}

my $header = 0;
while(<STDIN>)
{
	if(! $header)
	{
		if( ($negate_pat && ($_ !~ $pat)) || (! $negate_pat && ($_ =~ $pat)) )
		{
			#print STDERR "*** Pattern " . ($negate_pat?'!':'') . "/$pat/ matches $_\n";
			# end of header
			$header = 1;
			if($pos eq 'after')
			{
				print;
			}
			
			print $text;
			
			if($pos eq 'before')
			{
				print;
			}
		}
		else
		{
			print;
		}
	}
	else
	{
		print;
	}
}
