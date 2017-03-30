#!/usr/bin/perl
use strict;
use warnings;

# check for XML::Parser
# eval {
	# require XML::Parser;
	# XML::Parser->import;
# };
# if($@) { die "Couldn't load XML::Parser"; }

# check for XML::LibXML
eval {
	require XML::LibXML;
	XML::LibXML->import;
};
if($@) { die "Couldn't load XML::LibXML"; }

# globals
$::op = undef;
$::benchmark_file = undef;
$::log_fh = undef;
$::debug = 0;
$::noop = 0;
$::profile = undef;

# functions
sub print_log {
    my($msg) = @_;
    print STDERR $msg;
    if(defined($::log_fh))
    {
        print $::log_fh $msg;
    }
}

sub print_debug {
	my($msg) = @_;
	
	if($::debug) { print_log($msg); }
}

sub usage {
    die "Usage: $0 <operation> benchmark.xml [options] > results-xccdf.xml
  Status information is printed to STDERR and results are printed to STDOUT
  
  Operation:
	-c, --check     check the system against the benchmark
    -f, --fix       fix the system against the results benchmark
    --parse-only    just parse the benchmark file, don't check or fix

  Options:
    --profile       profile to select in the benchmark (mandatory if multiple profiles are defined)
    --log log_file  log status messages to the log_file
    --debug         turn on debugging message and stop after script failures
    --noop          don't perform fixes as part of fix operation
";
}

sub xml_escape {
	my ($msg) = @_;
	
	$msg =~ s/</&lt;/g;
	$msg =~ s/>/&gt;/g;
	$msg =~ s/&/&amp;/g;
	$msg =~ s/"/&quot;/g;
	$msg =~ s/'/&apos;/g;
	return $msg;
}

# from http://www.go4expert.com/articles/inarray-functionality-perl-t8978/
sub in_array {
     my ($arr,$search_for) = @_;
     return grep {$search_for eq $_} @$arr;
}

if(scalar(@ARGV) < 1)
{
    usage();
}

# parse options
for(my $i = 0; $i < scalar(@ARGV); $i++)
{
    if($ARGV[$i] =~ /-c|--check/)
    {
        $::op = 'check';
        
        if($i + 1 >= scalar(@ARGV))
        {
            die "No benchmark file specified\n";
        }
        
        $::benchmark_file = $ARGV[++$i];
    }
    elsif($ARGV[$i] =~ /-f|--fix/)
    {
        $::op = 'fix';
        
        if($i + 1 >= scalar(@ARGV))
        {
            die "No benchmark file specified\n";
        }
        
        $::benchmark_file = $ARGV[++$i];
    }
    elsif($ARGV[$i] =~ /--parse-only/)
    {
        $::op = 'parse-only';
        
        if($i + 1 >= scalar(@ARGV))
        {
            die "No benchmark file specified\n";
        }
        
        $::benchmark_file = $ARGV[++$i];
    }
    elsif($ARGV[$i] =~ /--debug/)
    {
        $::debug = 1;
    }
    elsif($ARGV[$i] =~ /--log/)
    {
        if($i + 1 >= scalar(@ARGV))
        {
            die "No log file specified\n";
        }
        
        if(! open($::log_fh, '>', $ARGV[$i+1]))
        {
            die "Couldn't open file $ARGV[$i+1]\n";
        }
        $i++;
    }
    elsif($ARGV[$i] =~ /--noop/)
    {
        $::noop = 1;
    }
    elsif($ARGV[$i] =~ /--profile/)
    {
         if($i + 1 >= scalar(@ARGV))
        {
            die "No profile specified\n";
        }
        
		$::profile = $ARGV[++$i]
    }
    else
    {
        warn "Unknown argument: $ARGV[$i]\n";
        usage();
    }
}

# check mandatory options
if(! defined($::op) || ! defined($::benchmark_file))
{
    usage();
}

# OS specific stuff
if($^O eq 'linux')
{
	$::username = getpwuid($<);
	
	if( ($::op eq 'check' || $::op eq 'fix') && $::username ne 'root')
	{
		die "Must be run as root to perform checks/fixes";
	}
	
	if($::username eq 'root')
	{
		$::privileged_user = 1;
	}
	else
	{
		$::privileged_user = 0;
	}

	use Sys::Hostname;
	$::hostname = hostname;

	@::ip_addrs = ();
	@::mac_addrs = ();
	foreach my $line (split /^/, `ip addr show`)
	{
		if($line =~ /[0-9]+: ([0-9a-zA-Z.-]+):/)
		{
		}
		elsif($line =~ /\s*inet ([0-9.]+)\//)
		{
			push @::ip_addrs, $1;
		}
		elsif($line =~ /\s*inet6 ([0-9:]+)\//)
		{
			push @::ip_addrs, $1;
		}
		elsif($line =~ /\s*link\/ether ([0-9a-fA-F:]+) /)
		{
			push @::mac_addrs, $1;
		}
	}

}
elsif($^O eq 'MSWin32')
{
	# $::username
	# $::privileged_user
	# $::hostname
	# @::ip_addrs
	# @::mac_addrs
}
else
{
	die "Unsupported operating system $^O";
}

# parse benchmark
# $::Benchmark_id = undef;
# %::profiles = ();
# $::cur_profile = undef;
# $::in_profile_title = 0;
# $::cur_group = undef;
# %::rules = ();
# $::cur_rule = undef;
# $::in_rule_version = 0;
# %::rule_results = ();
# $::cur_rule_result = undef;
# $::in_rule_result = 0;
# $::in_rule_message = 0;
# my $parser = XML::Parser->new(
    # ErrorContext => 2,
    # Handlers => {
		# Start=> sub {
			# my( $expat, $element, %attrs ) = @_;
			
			# if($element =~ /^.*[:]?Benchmark$/)
			# {
				# $::Benchmark_id = $attrs{'id'};
			# }
			# elsif($element =~ /^.*[:]?Profile$/)
			# {
				# $::cur_profile = $attrs{'id'};
				# $::profiles{$::cur_profile}{'selected'} = [];
				# $::profiles{$::cur_profile}{'title'} = '';
			# }
			# elsif(defined($::cur_profile) && $element =~ /^.*[:]?title$/)
			# {
				# $::in_profile_title = 1;
			# }
			# elsif(defined($::cur_profile) && $element =~ /^.*[:]?select$/)
			# {
				# if($attrs{'selected'} eq 'true')
				# {
					# push @{$::profiles{$::cur_profile}{'selected'}}, $attrs{'idref'};
				# }
			# }
			# elsif($element =~ /^.*[:]?Group$/)
			# {
				# if(defined($::cur_group)) { die "Nested groups are not supported yet, line " . $expat->current_line; }
				# $::cur_group = $attrs{'id'};
			# }
			# elsif($element =~ /^.*[:]?Rule$/)
			# {
				# $::cur_rule = $attrs{'id'};
				# $::rules{$::cur_rule}{'group'} = $::cur_group;
				# $::rules{$::cur_rule}{'version'} = '';
			# }
			# elsif(defined($::cur_rule) && $element =~ /^.*[:]?version$/)
			# {
				# $::in_rule_version = 1;
			# }
			# elsif($element =~ /^.*[:]?rule-result$/)
			# {
				# $::cur_rule_result = $attrs{'idref'};
				# $::rule_results{$::cur_rule_result}{'result'} = '';
				# $::rule_results{$::cur_rule_result}{'message'} = '';
			# }
			# elsif(defined($::cur_rule_result) && $element =~ /^.*[:]?result$/)
			# {
				# $::in_rule_result = 1;
			# }
			# elsif(defined($::cur_rule_result) && $element =~ /^.*[:]?message$/)
			# {
				# $::in_rule_message = 1;
			# }
		# },
        # End=>sub {
			# my( $expat, $element ) = @_;
			
			# if($element =~ /^.*[:]?Rule$/)
			# {
				# $::cur_rule = undef;
			# }
			# elsif(defined($::cur_rule) && $element =~ /^.*[:]?version$/)
			# {
				# $::in_rule_version = 0;
			# }
			# elsif($element =~ /^.*[:]?Profile$/)
			# {
				# $::cur_profile = undef;
			# }
			# elsif($element =~ /^.*[:]?Group$/)
			# {
				# $::cur_group = undef;
			# }
			# elsif(defined($::cur_profile) && $element =~ /^.*[:]?title$/)
			# {
				# $::in_profile_title = 0;
			# }
			# elsif($element =~ /^.*[:]?rule-result$/)
			# {
				# $::cur_rule_result = undef;
			# }
			# elsif(defined($::cur_rule_result) && $element =~ /^.*[:]?result$/)
			# {
				# $::in_rule_result = 0;
			# }
			# elsif(defined($::cur_rule_result) && $element =~ /^.*[:]?message$/)
			# {
				# $::in_rule_message = 0;
			# }
		# },
        # Char=>sub {
			# my( $expat, $string ) = @_;
			# if(defined($::cur_rule) && $::in_rule_version)
			# {
				# $::rules{$::cur_rule}{'version'} .= $string;
			# }
			# elsif(defined($::cur_rule_result) && $::in_rule_result)
			# {
				# $::rule_results{$::cur_rule_result}{'result'} .= $string;
			# }
			# elsif(defined($::cur_rule_result) && $::in_rule_message)
			# {
				# $::rule_results{$::cur_rule_result}{'message'} .= $string;
			# }
			# elsif(defined($::cur_profile) && $::in_profile_title)
			# {
				# $::profiles{$::cur_profile}{'title'} .= $string;
			# }
		# },
    # }
# );
# eval { $parser->parsefile( $::benchmark_file ); };

$::Benchmark_id = undef;
%::profiles = ();
%::rules = ();
%::rule_results = ();
my $xccdf_doc = XML::LibXML->new->parse_file($::benchmark_file);
my $xc = XML::LibXML::XPathContext->new($xccdf_doc);
$xc->registerNs('cdf', 'http://checklists.nist.gov/xccdf/1.1');
$::Benchmark_id = $xc->findvalue('//cdf:Benchmark/@id');
foreach my $profile ($xc->findnodes('//cdf:Profile'))
{
	my $id = $profile->getAttribute('id');
	$::profiles{$id}{'title'} = $xc->findvalue('//cdf:Profile[@id="' . $id . '"]/cdf:title');
	print_debug("Profile $id $::profiles{$id}{'title'}\n");
	foreach my $select($xc->findnodes('//cdf:Profile[@id="' . $id . '"]/cdf:select'))
	{
		push @{$::profiles{$id}{'selected'}}, $select->getAttribute('idref');
	}
	print_debug("Profile selected " . join(', ', @{$::profiles{$id}{'selected'}}) . "\n");
}
foreach my $group($xc->findnodes('//cdf:Group'))
{
	my $group_id = $group->getAttribute('id');
	print_debug("Group $group_id\n");
	foreach my $rule ($xc->findnodes('//cdf:Group[@id="' . $group_id . '"]/cdf:Rule'))
	{
		my $rule_id = $rule->getAttribute('id');
		$::rules{$rule_id}{'group'} = $group_id;
		$::rules{$rule_id}{'version'} = $xc->findvalue('//cdf:Rule[@id="' . $rule_id . '"]/cdf:version');
		print_debug("Rule $rule_id $::rules{$rule_id}{'group'} $::rules{$rule_id}{'version'}\n");
	}
}
foreach my $rr($xc->findnodes('//cdf:rule-result'))
{
	my $rr_id = $rr->getAttribute('idref');
	$::rule_results{$rr_id}{'result'} = $xc->findvalue('//cdf:rule-result[@idref="' . $rr_id . '"]/cdf:result');
	$::rule_results{$rr_id}{'message'} = $xc->findvalue('//cdf:rule-result[@idref="' . $rr_id . '"]/cdf:message');
	print_debug("rule-result $rr_id $::rule_results{$rr_id}{'result'} $::rule_results{$rr_id}{'message'}\n");
}

if( (scalar(keys(%::profiles)) > 1 && ! defined($::profile))
	|| (defined($::profile) && ! exists($::profiles{$::profile})) )
{
	print STDERR "No profile selected from below: \n\t" . join("\n\t", keys %::profiles) . "\n";
	exit;
}
elsif(scalar(keys(%::profiles)) == 1 && ! defined($::profile))
{
	$::profile = (keys %::profiles)[0];
	print_log("Selecting profile $::profile\n");
}
elsif(! defined($::profile))
{
	print_log("No profiles to select.\n");
}
else
{
	print_log("Selecting profile $::profile\n");
}

# report any error that stopped parsing
if( $@ ) {
    $@ =~ s/at \/.*?$//s;               # remove module line number
    die "\nERROR in '$::benchmark_file':\n$@\n";
}

# get system info
my $success_count = 0;
my $rule_count = 0;
my %result_counts = ();

if($::op eq 'parse-only')
{
    print_log("Parsing completed successfully\n");
    print_log(scalar(keys(%::rules)) . " rules loaded\n");
    print_log(scalar(keys(%::rule_results)) . " rule results loaded\n");
    exit;
}
elsif($::op eq 'check')
{
	# run answer file
	my $answer_file;
	if($^O eq 'linux')
	{
		$answer_file = "answer/check_$::Benchmark_id.pl";
	}
	elsif($^O eq 'MSWin32')
	{
		$answer_file = "answer\\check_$::Benchmark_id.pl";
	}
	$answer_file =~ s/ /_/g;
	if(-f $answer_file)
	{
		print_log("Loading answer file $answer_file\n");
		eval `perl $answer_file`;
	}
	else
	{
		print_log("No answer file $answer_file\n");
	}

	# run tests
	my $start_time = scalar(localtime());
	my @selected_rules = ();
	if(defined($::profile))
	{
		foreach my $rule_id (sort keys(%::rules))
		{
			if(grep {$_ eq $::rules{$rule_id}{'group'}} @{$::profiles{$::profile}{'selected'}})
			{
				push @selected_rules, $rule_id;
			}
		}
	}
	else
	{
		@selected_rules = sort keys(%::rules);
	}
	
	foreach my $rule_id (@selected_rules)
	{
		my ($check_script, $check_cmd);
		if($^O eq 'linux')
		{
			$check_script = $::Benchmark_id;
			$check_script =~ s/ /_/g;
			$check_script = "check/$check_script/$rule_id.sh";
			$check_cmd = "sh $check_script";
		}
		elsif($^O eq 'MSWin32')
		{
			$check_script = $::Benchmark_id;
			$check_script =~ s/ /_/g;
			$check_script = "check\\$check_script\\$rule_id.bat";
			$check_cmd = "$check_script";
		}
		else
		{
			print STDERR "Unsupported operating system $^O\n";
			exit 1;
		}
		
		print_log("Checking rule $rule_id...");
		if(! -f $check_script)
		{
			$::rules{$rule_id}{'result'} = 'notchecked';
			$::rules{$rule_id}{'message'} = "No script for rule $rule_id";
			$::rules{$rule_id}{'check'} = '';
		}
		else
		{
			my $out = `$check_cmd`;
			$::rules{$rule_id}{'check'} = xml_escape($check_cmd);
			$out =~ m|<result>([^<]+)</result>|;
			my $result = $1;
			
			if(! defined($result))
			{
				$::rules{$rule_id}{'result'} = 'error';
				my $cherr = $? >> 8;
				$::rules{$rule_id}{'message'} = "Didn't get a result from check script $rule_id; output was '$out'; result code: $cherr; cmd: $check_cmd";
				if($::debug) { print_log("Press enter to continue:"); <STDIN>; }
			}
			elsif($result !~ /^(pass|fail|notapplicable|notchecked|error|unknown|notselected|informational|fixed)$/)
			{
				$::rules{$rule_id}{'result'} = 'error';
				$::rules{$rule_id}{'message'} = "Got an invalid result from check script $rule_id: $result";
				if($out =~ m|<message>([^<]+)</message>|)
				{
					$::rules{$rule_id}{'message'} .= ":$1";
				}
				if($::debug) { print_log("Press enter to continue:"); <STDIN>; }
			}
			else
			{
			
				$::rules{$rule_id}{'result'} = $result;
				
				if($result =~ /^(pass|notapplicable|informational|fixed)$/)
				{
					$success_count ++;
				}
				elsif($result =~ /^fail$/)
				{
					if($out =~ m|<message>([^<]+)</message>|)
					{
						$::rules{$rule_id}{'message'} = $1;
					}
					else
					{
						$::rules{$rule_id}{'result'} = 'error';
						$::rules{$rule_id}{'message'} = "Got an fail result without a message from check script $rule_id: $result";
						if($::debug) { print_log("Press enter to continue:"); <STDIN>; }
					}
				}
				else
				{
					if($out =~ m|<message>([^<]+)</message>|)
					{
						$::rules{$rule_id}{'message'} = $1;
					}
					# notchecked, error, unknown, notselected
				
				}
			}
		}
		$result_counts{$::rules{$rule_id}{'result'}}++;
		
		print_log($::rules{$rule_id}{'result'});
		if(exists($::rules{$rule_id}{'message'}))
		{
			print_log(": " . $::rules{$rule_id}{'message'});
		}
		print_log("\n");
		$rule_count ++;
	}
	my $end_time = scalar(localtime());


	print '<?xml version="1.0" encoding="utf-8"?>', "\n",
	'<?xml-stylesheet href="STIG_results.xsl" type="text/xsl"?>', "\n",
	'<Benchmark xmlns:dsig="http://www.w3.org/2000/09/xmldsig#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cpe="http://cpe.mitre.org/language/2.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xml:lang="en" xsi:schemaLocation="http://checklists.nist.gov/xccdf/1.1 http://nvd.nist.gov/schema/xccdf-1.1.4.xsd http://cpe.mitre.org/dictionary/2.0 http://cpe.mitre.org/files/cpe-dictionary_2.1.xsd" xmlns="http://checklists.nist.gov/xccdf/1.1" id="', $::Benchmark_id, '">', "\n",
	'<TestResult id="', $::Benchmark_id, '_testresult" start-time="', $start_time, '" end-time="', $end_time, '" xmlns:xccdf="http://checklists.nist.gov/xccdf/1.2" version="1.0">', "\n",
	'<identity authenticated="1" privileged="', $::privileged_user, '">', $::username, "</identity>\n",
	'<target>', $::hostname, "</target>\n";
	
	if(defined($::profile))
	{
		print '<profile>', $::profile, '</profile>';
	}

	foreach(@::ip_addrs)
	{
		print "<target-address>$_</target-address>\n";
	}

	print "<target-facts>\n";
	foreach(@::mac_addrs)
	{
		print "\t", '<fact type="string" name="urn:fact:ethernet:MAC">', $_, "</fact>\n";
	}
	print "</target-facts>\n";

	foreach(@selected_rules)
	{
		print '<rule-result idref="', $_, '" time="', scalar(localtime()), '" version="', $::rules{$_}{'version'}, '">';
		print "\t<result>", $::rules{$_}{'result'}, "</result>\n";
		if(exists($::rules{$_}{'message'}))
		{
			print "\t<message>", $::rules{$_}{'message'}, '</message>', "\n";
		}
		print "\t<check>", $::rules{$_}{'check'}, '</check>', "\n";
		print "</rule-result>\n";
	}

	print "</TestResult>\n</Benchmark>\n";

	foreach my $k (keys %result_counts)
	{
		print_log("$result_counts{$k} $k results\n");
	}
	print_log("$rule_count total results\n"); 
	print_log(($success_count / scalar(keys(%::rules))) * 100 . "%\n");
}
elsif($::op eq 'fix')
{
	# run check answer file
	my $answer_file;
	if($^O eq 'linux')
	{
		$answer_file = "answer/check_$::Benchmark_id.pl";
	}
	elsif($^O eq 'MSWin32')
	{
		$answer_file = "answer\\check_$::Benchmark_id.pl";
	}
	$answer_file =~ s/ /_/g;
	if(-f $answer_file)
	{
		print_log("Loading answer file $answer_file\n");
		eval `perl $answer_file`;
	}
	else
	{
		print_log("No answer file $answer_file\n");
	}

	# run fix answer file
	if($^O eq 'linux')
	{
		$answer_file = "answer/fix_$::Benchmark_id.pl";
	}
	elsif($^O eq 'MSWin32')
	{
		$answer_file = "answer\\fix_$::Benchmark_id.pl";
	}
	$answer_file =~ s/ /_/g;
	if(-f $answer_file)
	{
		print_log("Loading answer file $answer_file\n");
		eval `perl $answer_file`;
	}
	else
	{
		print_log("No answer file $answer_file\n");
	}
	
	RULE: foreach(sort keys(%::rule_results))
	{
		if($::rule_results{$_}{'result'} =~ /^(pass|notapplicable|informational|fixed)$/)
		{
			print_log("Skipping $::rule_results{$_}{'result'} result for rule $_\n");
			next RULE;
		}
		
		if($::rule_results{$_}{'result'} eq 'fail')
		{
			my ($fix_script, $check_script);
			if($^O eq 'linux')
			{
				$fix_script = "fix/$_.sh";

				$fix_script = $::Benchmark_id;
				$fix_script =~ s/ /_/g;
				$fix_script = "fix/$fix_script/$_.sh";

				$check_script = $::Benchmark_id;
				$check_script =~ s/ /_/g;
				$check_script = "check/$check_script/$_.sh";
				
				$::fix_cmd = "sh $fix_script";
				$::check_cmd = "sh $check_script";
			}
			elsif($^O eq 'MSWin32')
			{
				$fix_script = "fix\\$_.bat";

				$fix_script = $::Benchmark_id;
				$fix_script =~ s/ /_/g;
				$fix_script = "fix\\$fix_script\\$_.bat";

				$check_script = $::Benchmark_id;
				$check_script =~ s/ /_/g;
				$check_script = "check\\$check_script\\$_.bat";
				
				$::fix_cmd = "$fix_script";
				$::check_cmd = "$check_script";
			}
			
			if(! -f $check_script)
			{
				print_log("No check for rule $_\n");
			}
			elsif(! -f $fix_script)
			{
				print_log("No fix for rule $_: $::rule_results{$_}{'message'}\n");
			}
			else
			{
				print_log("Checking rule $_...");
				my $out = `$::check_cmd`;
				chomp $out;
				$out =~ m|<result>([^<]+)</result>|;
				my $result = $1;
				my $message = '';
				if($out =~ m|<message>([^<]+)</message>|)
				{
					print_log("$1\n");
				}
				
				if($result eq "pass")
				{
					print_log("Fix already applied for $_\n");
					$success_count ++;
				}
				else
				{
					print_log("Fixing rule $_: $::rule_results{$_}{'message'}...\n");
					
					my $err;
					if($::noop)
					{
						$err = 0;
					}
					else
					{
						#$out = `$::fix_cmd`;
						#print_log($out);
						#$err = $?;
						$err = system($::fix_cmd);
					}
					
					$out = `$::check_cmd`;
					chomp $out;
					$out =~ m|<result>([^<]+)</result>|;
					$result = $1;
					$out =~ m|<message>([^<]+)</message>|;
					$message = $1;
					
					if($err == 0 && $result eq "pass")
					{
						print_log("Fix for $_ successful\n");
						$success_count ++;
					}
					else
					{
						print_log("*** Fix for $_ failed, exit $err, result $result, message $message\n");
						if($::debug) { print_log("Press enter to continue:"); <STDIN>; }
					}
				}
			}
			$rule_count ++;
		}
	}

	if($rule_count == 0)
	{
		print_log("No rules to fix\n");
	}
	else
	{
		print_log("$success_count of $rule_count fixed: "); 
		my $p = ($success_count / $rule_count) * 100;
		print_log("$p%\n");
	}
}

if(defined($::log_fh))
{
    close($::log_fh);
}
