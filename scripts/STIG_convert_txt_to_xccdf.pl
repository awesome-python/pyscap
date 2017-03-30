#!/usr/bin/perl
use strict;
use warnings;

if(scalar(@ARGV) < 1)
{
	print STDERR "Usage: $0 benchmark.txt [--parse-only] [--log log_file]\n";
	exit 1;
}

my $file = shift @ARGV;
my $parse_only = 0;
my $debug = 0;
my $log = undef;

sub print_log {
	my($msg) = @_;
	print STDERR $msg;
	if(defined($log))
	{
		print $log $msg;
	}
}

sub print_debug {
	my($msg) = @_;
	print STDERR $msg if $debug;
}

sub convert_severity {
	my($s) = @_;
	
	if($s =~ /Category III/)
	{
		return 'low';
	}
	elsif($s =~ /Category II/)
	{
		return 'medium';
	}
	elsif($s =~ /Category I/)
	{
		return 'high';
	}
	else
	{
		die "Unknown severity $s\n";
	}
}


sub trim {
	my($s) = @_;
	
	$s =~ s/^\s+|\s+$//g;
	return $s;
}

$::parse_state = '';

sub parse_line {
	my($line, $last_line) = @_;
	$_ = $line;
	
	if(/^Checklist:\s+(.*?)\s+$/)
	{
		$::Benchmark_id = $1;
	}
	elsif(/^Vulnerability Key: (.*) STIG ID: (.*) Release Number: (.*) Status: (.*) Short Name: (.*) Long Name: (.*)$/)
	{
		$::cur_group = $1;
		$::parse_state = '';
		print_debug("\nGroup $::cur_group\n");
		$::groups->{$::cur_group} = {'id' => $1};
		$::groups->{$::cur_group}->{'title'} = $5;
		$::groups->{$::cur_group}->{'description'} = $6;
	}
	elsif(/^Vulnerability Key: (.*) STIG ID: (.*) Release Number: (.*) Status: (.*) Short Name: (.*)$/)
	{
		$::cur_group = $1;
		$::parse_state = '';
		print_debug("\nGroup $::cur_group\n");
		$::groups->{$::cur_group} = {'id' => $1};
		$::groups->{$::cur_group}->{'title'} = $5;
	}
	elsif(/^Vulnerability Key:\s*(.*) STIG\s+ID:\s*(.*)\s*Release Number:\s*(.*)$/)
	{
		$::cur_group = $1;
		$::parse_state = '';
		print_debug("\nGroup $::cur_group\n");
		$::groups->{$::cur_group} = {'id' => $1};
	}
	elsif(/^Vulnerability Key:\s*(.*)\s*STIG\s+ID:\s*(.*)$/)
	{
		$::cur_group = $1;
		$::parse_state = '';
		print_debug("\nGroup $::cur_group\n");
		$::groups->{$::cur_group} = {'id' => $1};
	}
	elsif(/^Vulnerability Key:\s*(.*)$/)
	{
		$::cur_group = $1;
		$::parse_state = '';
		print_debug("\nGroup $::cur_group\n");
		$::groups->{$::cur_group} = {'id' => $1};
	}
	elsif(defined($::cur_group))
	{
		if(! exists($::groups->{$::cur_group}->{'rule'}))
		{
			if($::parse_state eq 'in desc')
			{
				if(/(.*)IA Controls:/)
				{
					$::groups->{$::cur_group}->{'description'} .= $1;
					$::groups->{$::cur_group}->{'description'} = $::groups->{$::cur_group}->{'description'};
					$::parse_state = '';
					print_debug("End Group Desc: $::groups->{$::cur_group}->{'description'}\n");
				}
				else
				{
					$::groups->{$::cur_group}->{'description'} .= $_;
				}
			}
			elsif(/^Status: (.*) Short Name: (.*) Long Name: (.*)$/)
			{
				$::groups->{$::cur_group}->{'title'} = $2;
				print_debug("Group Title: $::groups->{$::cur_group}->{'title'}\n");
				$::groups->{$::cur_group}->{'description'} = $3;
				print_debug("Group Desc: $::groups->{$::cur_group}->{'description'}\n");
				$::parse_state = 'in desc';
			}
			elsif(/^Status: (.*) Short Name: (.*)$/)
			{
				$::groups->{$::cur_group}->{'title'} = $2;
				print_debug("Group Title: $::groups->{$::cur_group}->{'title'}\n");
			}
			elsif(/^Short Name:\s*(.*?)\s*Long Name:\s*(.*)IA Controls:(.*)$/)
			{
				$::groups->{$::cur_group}->{'title'} = $1;
				print_debug("Group Title: $::groups->{$::cur_group}->{'title'}\n");
				$::groups->{$::cur_group}->{'description'} = $2;
				print_debug("Group Desc: $::groups->{$::cur_group}->{'description'}\n");
			}
			elsif(/^Short Name:\s*(.*?)$/)
			{
				$::groups->{$::cur_group}->{'title'} = $1;
				print_debug("Group Title: $::groups->{$::cur_group}->{'title'}\n");
			}
			elsif(/^Release Number: (.*) Status: (.*) Short Name: (.*) Long Name: (.*)$/)
			{
				$::groups->{$::cur_group}->{'title'} = $3;
				print_debug("Group Title: $::groups->{$::cur_group}->{'title'}\n");
				$::groups->{$::cur_group}->{'description'} = $4;
				print_debug("Group Desc: $::groups->{$::cur_group}->{'description'}\n");
			}
			elsif(/^Release Number: (.*) Status: (.*) Short Name: (.*)$/)
			{
				$::groups->{$::cur_group}->{'title'} = $3;
				print_debug("Group Title: $::groups->{$::cur_group}->{'title'}\n");
			}
			elsif(/^Long Name:\s*(.*?)IA Controls\s*(.*)$/)
			{
				$::groups->{$::cur_group}->{'description'} = $1;
				print_debug("Group desc $::groups->{$::cur_group}->{'description'}\n");
			}
			elsif(/^Long Name:\s*(.*?)$/)
			{
				$::groups->{$::cur_group}->{'description'} = $1;
				$::parse_state = 'in desc';
			}
			elsif($last_line =~ /^Vulnerability Key:/
				&& /^STIG ID:\s*(.*)/)
			{
				print_debug("skip STIG ID, we're still in the group header");
			}
			elsif(/^STIG ID:\s*(.*)\s*Last Updated: (.*)\s*Severity: (.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'id'} = $1;
				print_debug("Rule $::groups->{$::cur_group}->{'rule'}->{'id'}\n");
				$::groups->{$::cur_group}->{'rule'}->{'severity'} = convert_severity($3);
				print_debug("Rule severity $::groups->{$::cur_group}->{'rule'}->{'severity'}\n");
				$::groups->{$::cur_group}->{'rule'}->{'version'} = $1;
				print_debug("Rule version $::groups->{$::cur_group}->{'rule'}->{'version'}\n");
			}
			elsif(/^STIG ID:\s*(.*?)\s*Last Updated:\s*(.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'id'} = $1;
				print_debug("Rule $::groups->{$::cur_group}->{'rule'}->{'id'}\n");
				$::groups->{$::cur_group}->{'rule'}->{'version'} = $1;
				print_debug("Rule version $::groups->{$::cur_group}->{'rule'}->{'version'}\n");
			}
			elsif(/^STIG ID:\s*(.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'id'} = $1;
				print_debug("Rule $::groups->{$::cur_group}->{'rule'}->{'id'}\n");
				$::groups->{$::cur_group}->{'rule'}->{'version'} = $1;
				print_debug("Rule version $::groups->{$::cur_group}->{'rule'}->{'version'}\n");
			}
		}
		else
		{
			if($::parse_state eq 'in r title')
			{
				if(/(.*)\s*Vulnerability\s*(.*)/)
				{
					$::groups->{$::cur_group}->{'rule'}->{'title'} .= $1;
					print_debug("End Rule Title: $::groups->{$::cur_group}->{'rule'}->{'title'}\n");
					$::parse_state = 'in r desc';
					parse_line($2);
					return;
				}
				
				
				if(/(.*)\s*Discussion:\s*(.*)/)
				{
					$::groups->{$::cur_group}->{'rule'}->{'description'} .= $1;
					$::parse_state = 'in r desc';
					parse_line($2);
					return
				}
				
				
				if(/(.*)Default Finding/)
				{
					parse_line($1);
					$::groups->{$::cur_group}->{'rule'}->{'title'} .= $1;
					print_debug("End Rule Title: $::groups->{$::cur_group}->{'rule'}->{'title'}\n");
					$::groups->{$::cur_group}->{'rule'}->{'description'} = '';
					$::parse_state = '';
					return;
				}
				else
				{
					$::groups->{$::cur_group}->{'rule'}->{'title'} .= $_;
				}
			}
			elsif($::parse_state eq 'in r desc')
			{
				if(/(.*)\s*Discussion:\s*(.*)/)
				{
					$::groups->{$::cur_group}->{'rule'}->{'description'} .= $1;
					parse_line($2);
					return;
				}
				
				if(/(.*)Default Finding/)
				{
					$::groups->{$::cur_group}->{'rule'}->{'description'} .= $1;
					print_debug("End Rule Desc: $::groups->{$::cur_group}->{'rule'}->{'description'}\n");
					$::parse_state = '';
				}
				else
				{
					$::groups->{$::cur_group}->{'rule'}->{'description'} .= $_;
				}
			}
			elsif($::parse_state eq 'in check')
			{
				if(/^([a-zA-Z0-9-]+\s*\([a-zA-Z]+\))\s*(.*)$/)
				{
					$::groups->{$::cur_group}->{'rule'}->{'check'}->{'system'} = $1;
					print_debug("Check sys $::groups->{$::cur_group}->{'rule'}->{'check'}->{'system'}\n");
					$::groups->{$::cur_group}->{'rule'}->{'check'}->{'check-content'} = $2;
				}
				else
				{
					$::groups->{$::cur_group}->{'rule'}->{'check'}->{'system'} = $_;
					print_debug("Check sys $::groups->{$::cur_group}->{'rule'}->{'check'}->{'system'}\n");
				}
				$::parse_state = 'in check content';
			}
			elsif($::parse_state eq 'in check content')
			{
				if(/^Fixes:\s*([a-zA-Z0-9-]+\s*\([a-zA-Z]+\))\s*(.*)$/)
				{
					print_debug("Check txt $::groups->{$::cur_group}->{'rule'}->{'check'}->{'check-content'}\n");
					$::groups->{$::cur_group}->{'rule'}->{'fix'}->{'id'} = $1;
					print_debug("Fix id $::groups->{$::cur_group}->{'rule'}->{'fix'}->{'id'}\n");
					$::groups->{$::cur_group}->{'rule'}->{'fix'}->{'fixtext'} = $2;
					$::parse_state = 'in fix text';
				}
				elsif(/^Fixes:(.*)/)
				{
					print_debug("Check txt $::groups->{$::cur_group}->{'rule'}->{'check'}->{'check-content'}\n");
					$::parse_state = 'in fix';
				}
				else
				{
					$::groups->{$::cur_group}->{'rule'}->{'check'}->{'check-content'} .= $_;
				}
			}
			elsif($::parse_state eq 'in fix')
			{
				if(/^([a-zA-Z0-9-]+\s*\([a-zA-Z]+\))\s*(.*)$/)
				{
					$::groups->{$::cur_group}->{'rule'}->{'fix'}->{'id'} = $1;
					print_debug("Fix id $::groups->{$::cur_group}->{'rule'}->{'fix'}->{'id'}\n");
					$::groups->{$::cur_group}->{'rule'}->{'fix'}->{'fixtext'} = $2;
				}
				else
				{
					$::groups->{$::cur_group}->{'rule'}->{'fix'}->{'id'} = $_;
					print_debug("Fix id $::groups->{$::cur_group}->{'rule'}->{'fix'}->{'id'}\n");
				}
				$::parse_state = 'in fix text';
			}
			elsif($::parse_state eq 'in fix text')
			{
				if(/^https:/)
				{
					print_debug("Fix text $::groups->{$::cur_group}->{'rule'}->{'fix'}->{'fixtext'}\n");
					$::parse_state = '';
					parse_line($_);
					return;
				}
				elsif(/^Vulnerability Key:/)
				{
					print_debug("Fix text $::groups->{$::cur_group}->{'rule'}->{'fix'}->{'fixtext'}\n");
					$::parse_state = '';
					parse_line($_);
					return;
				}
				else
				{
					$::groups->{$::cur_group}->{'rule'}->{'fix'}->{'fixtext'} .= $_;
				}
			}
			elsif($::parse_state ne '')
			{
				die "Invalid parse state: $::parse_state\n";
			}
			elsif(/^Long Name:\s*(.*?)Vulnerability\s*(.*)Discussion:\s*(.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'title'} = $1;
				print_debug("Rule title $::groups->{$::cur_group}->{'rule'}->{'title'}\n");
				$::groups->{$::cur_group}->{'rule'}->{'description'} = $2 . $3;
				$::parse_state = 'in r desc';
			}
			elsif(/^Long Name:\s*(.*?)Vulnerability\s*(.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'title'} = $1;
				print_debug("Rule title $::groups->{$::cur_group}->{'rule'}->{'title'}\n");
				$::groups->{$::cur_group}->{'rule'}->{'description'} = $2;
				$::parse_state = 'in r desc';
			}
			elsif(/^Long Name:\s*(.*?)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'title'} = $1;
				$::parse_state = 'in r title';
			}
			elsif(/^Last Updated:\s*(.*?)Severity: (.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'severity'} = convert_severity($2);
				print_debug("Rule severity $::groups->{$::cur_group}->{'rule'}->{'severity'}\n");
			}
			elsif(/^Severity: (.*)$/)
			{
				$::groups->{$::cur_group}->{'rule'}->{'severity'} = convert_severity($1);
				print_debug("Rule severity $::groups->{$::cur_group}->{'rule'}->{'severity'}\n");
			}
			elsif(/^Checks/)
			{
				$::parse_state = 'in check';
			}
			elsif(/^STIG ID/)
			{
				$::cur_group = undef;
				parse_line($_);
				return;
			}
		}
	}
}

for(my $i=0; $i <scalar(@ARGV); $i++)
{
	my $arg = $ARGV[$i];
	if($arg =~ /--parse-only/)
	{
		$parse_only = 1;
	}
	elsif($arg =~ /--debug/)
	{
		$debug = 1;
	}
	elsif($arg =~ /--log/)
	{
		if($i + 1 >= scalar(@ARGV))
		{
			die "No log file specified\n";
		}
		
		if(! open($log, '>', $ARGV[$i+1]))
		{
			die "Couldn't open file $ARGV[$i+1]\n";
		}
	}
}

if(! -f $file)
{
	die "Couldn't open $file";
}

open my $fh, '<', $file or die "Couldn't open $file";

$::groups = {};
my $last_line;

$::cur_group = undef;

while(<$fh>)
{
	parse_line($_, $last_line);
	$last_line = $_;
}

close $fh;
use XML::LibXML;
my $doc = XML::LibXML::Document->new('1.0','utf-8');
my $pi = $doc->createProcessingInstruction("xml-stylesheet");
$pi->setData(type=>'text/xsl', href=>'STIG_unclass.xsl');
$doc->appendChild($pi);
my $benchmark = $doc->createElement('Benchmark');
$doc->setDocumentElement($benchmark);
$benchmark->setNamespace('http://www.w3.org/2000/09/xmldsig#', 'dsig');
$benchmark->setNamespace('http://www.w3.org/1999/xhtml', 'xhtml');
$benchmark->setNamespace('http://www.w3.org/2001/XMLSchema-instance', 'xsi');
$benchmark->setNamespace('http://cpe.mitre.org/language/2.0', 'cpe');
$benchmark->setNamespace('http://purl.org/dc/elements/1.1/', 'dc');
$benchmark->setNamespace('http://checklists.nist.gov/xccdf/1.1');
$benchmark->setAttribute('xml:lang', 'en');
$benchmark->setAttribute('xsi:schemaLocation', 'http://checklists.nist.gov/xccdf/1.1 http://nvd.nist.gov/schema/xccdf-1.1.4.xsd http://cpe.mitre.org/dictionary/2.0 http://cpe.mitre.org/files/cpe-dictionary_2.1.xsd');
$benchmark->setAttribute('id', trim($::Benchmark_id));

foreach my $k (keys %{$::groups})
{
	if(! defined($::groups->{$k}->{'id'})) { die "Undefined id for group $k\n"; }
	my $group = $doc->createElement('Group');
	$benchmark->addChild($group);
	$group->setAttribute('id', trim($::groups->{$k}->{'id'}));

	if( ! defined($::groups->{$k}->{'title'})) { die "Undefined title for group $k\n"; }
	$group->appendTextChild('title', trim($::groups->{$k}->{'title'}));

	if( ! defined($::groups->{$k}->{'description'})) { die "Undefined desc for group $k\n"; }
	$group->appendTextChild('description', trim($::groups->{$k}->{'description'}));

	if( ! defined($::groups->{$k}->{'rule'}->{'id'})) { die "Undefined rule id for group $k\n"; }

	if( ! defined($::groups->{$k}->{'rule'}->{'severity'})) { die "Undefined rule severity for group $k\n"; }
	my $rule = $doc->createElement('Rule');
	$group->addChild($rule);
	$rule->setAttribute('id', trim($::groups->{$k}->{'rule'}->{'id'}));
	$rule->setAttribute('severity', $::groups->{$k}->{'rule'}->{'severity'});
	$rule->setAttribute('weight', '10.0');

	if( ! defined($::groups->{$k}->{'rule'}->{'version'})) { die "Undefined rule version for group $k\n"; }
	$rule->appendTextChild('version', trim($::groups->{$k}->{'rule'}->{'version'}));

	if( ! defined($::groups->{$k}->{'rule'}->{'title'})) { die "Undefined rule title for group $k\n"; }
	my $r_title = $doc->createElement('title');
	$rule->addChild($r_title);
	$r_title->appendTextNode(trim($::groups->{$k}->{'rule'}->{'title'}));

	if( ! defined($::groups->{$k}->{'rule'}->{'description'})) { die "Undefined rule desc for group $k\n"; }
	my $r_desc = $doc->createElement('description');
	$rule->addChild($r_desc);
	$r_desc->appendTextNode(trim($::groups->{$k}->{'rule'}->{'description'}));

	# <reference>
		# <dc:title>VMS Target SRG-APP-DB</dc:title>
		# <dc:publisher>DISA FSO</dc:publisher>
		# <dc:type>VMS Target</dc:type>
		# <dc:subject>SRG-APP-DB</dc:subject>
		# <dc:identifier>2219</dc:identifier>
	# </reference>

	# <ident system="http://iase.disa.mil/cci">CCI-000054</ident>

	# <fixtext fixref="F-36081r1_fix">Limit concurrent connections for each system account to a number less than or equal to the organization defined number of sessions.</fixtext>
	# <fix id="F-36081r1_fix" />
	if( ! defined($::groups->{$k}->{'rule'}->{'fix'}->{'id'})) { die "Undefined rule fix id for group $k\n"; }
	if( ! defined($::groups->{$k}->{'rule'}->{'fix'}->{'fixtext'})) { die "Undefined rule fix text for group $k\n"; }
	my $r_fixtext = $doc->createElement('fixtext');
	$rule->addChild($r_fixtext);
	$r_fixtext->setAttribute('fixref', trim($::groups->{$k}->{'rule'}->{'fix'}->{'id'}));
	$r_fixtext->appendTextNode(trim($::groups->{$k}->{'rule'}->{'fix'}->{'fixtext'}));
	
	my $r_fix = $doc->createElement('fix');
	$rule->addChild($r_fix);
	$r_fix->setAttribute('id', trim($::groups->{$k}->{'rule'}->{'fix'}->{'id'}));

	if( ! defined($::groups->{$k}->{'rule'}->{'check'}->{'system'})) { die "Undefined rule check system for group $k\n"; }
	my $r_check = $doc->createElement('check');
	$rule->addChild($r_check);
	$r_check->setAttribute('system', trim($::groups->{$k}->{'rule'}->{'check'}->{'system'}));
	
		# <check-content-ref name="M" href="VMS_XCCDF_Benchmark_Database Generic SRG.xml" />
		
	if( ! defined($::groups->{$k}->{'rule'}->{'check'}->{'check-content'})) { die "Undefined rule check content for group $k\n"; }
	my $c_content = $doc->createElement('check-content');
	$r_check->addChild($c_content);
	$c_content->appendTextNode(trim($::groups->{$k}->{'rule'}->{'check'}->{'check-content'}));
}
my $txt = $doc->toString(2);
$txt =~ tr/\x91\x92\x{2018}\x{2019}/'/;
$txt =~ tr/\x93\x94\xab\x{201C}\x{201D}/"/;
$txt =~ tr/\xad\x96\x97\x{2013}\x{2014}/-/;
print $txt;

print_log(scalar(keys %{$::groups}) . " groups\n");

if(defined($log))
{
	close($log);
}
