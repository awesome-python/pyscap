#!/usr/bin/perl
use strict;
use warnings;

# check for XML::LibXML
eval {
	require XML::LibXML;
	XML::LibXML->import;
};
if($@) { die "Couldn't load XML::LibXML"; }

use Sys::Hostname;


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

# parse benchmark
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

# add system info
if($^O ne 'linux' && $^O ne 'MSWin32')
{
	die "Unsupported operating system $^O";
}

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
		$::rules{$rule_id}{'time'} = scalar(localtime());
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

	my $pi = $xccdf_doc->createProcessingInstruction("xml-stylesheet");
	$pi->setData(type=>'text/xsl', href=>'STIG_results.xsl');
	my $b_el = ($xc->findnodes('//cdf:Benchmark'))[0];
	$xccdf_doc->insertBefore($pi, $b_el);
	
	# add test results
	my $tr_el = XML::LibXML::Element->new('TestResult');
	$tr_el->setAttribute('id', $::Benchmark_id . '_' . $::profile);
	$tr_el->setAttribute('start-time', $start_time);
	$tr_el->setAttribute('end-time', $end_time);
	$tr_el->setAttribute('version', '1.0');
	$b_el->addChild($tr_el);
	
	my $tr_id_el = XML::LibXML::Element->new('identity');
	if($^O eq 'linux')
	{
		my $username = getpwuid($<);
		$tr_id_el->setAttribute('authenticated', '1');
		if($username eq 'root')
		{
			$tr_id_el->setAttribute('privileged', '1');
		}
		else
		{
			$tr_id_el->setAttribute('privileged', '0');
		}
		$tr_id_el->appendText($username);
	}
	elsif($^O eq 'MSWin32')
	{
		my $username = Win32::LoginName();
		if($username ne 'Guest')
		{
			$tr_id_el->setAttribute('authenticated', '1');
		}
		else
		{
			$tr_id_el->setAttribute('authenticated', '0');
		}
		if(Win32::IsAdminUser())
		{
			$tr_id_el->setAttribute('privileged', '1');
		}
		else
		{
			$tr_id_el->setAttribute('privileged', '0');
		}
		$tr_id_el->appendText(Win32::DomainName() . '\\' . $username);
	}
	$tr_el->addChild($tr_id_el);
	
	my $tr_t_el = XML::LibXML::Element->new('target');
	$tr_t_el->appendText(hostname);
	$tr_el->addChild($tr_t_el);
	
	if(defined($::profile))
	{
		my $tr_p_el = XML::LibXML::Element->new('profile');
		$tr_p_el->appendText($::profile);
		$tr_el->addChild($tr_p_el);
	}

	my $tr_tf_el = XML::LibXML::Element->new('target-facts');
	if($^O eq 'linux')
	{
		foreach my $line (split /^/, `ip addr show`)
		{
			if($line =~ /[0-9]+: ([0-9a-zA-Z.-]+):/) {}
			elsif($line =~ /\s*inet ([0-9.]+)\//)
			{
				my $tr_ta_el = XML::LibXML::Element->new('target-address');
				$tr_ta_el->appendText($1);
				$tr_el->addChild($tr_ta_el);
			}
			elsif($line =~ /\s*inet6 ([0-9:]+)\//)
			{
				my $tr_ta_el = XML::LibXML::Element->new('target-address');
				$tr_ta_el->appendText($1);
				$tr_el->addChild($tr_ta_el);
			}
			elsif($line =~ /\s*link\/ether ([0-9a-fA-F:]+) /)
			{
				my $f_el = XML::LibXML::Element->new('fact');
				$f_el->setAttribute('type', 'string');
				$f_el->setAttribute('name', 'urn:fact:ethernet:MAC');
				$f_el->appendText($1);
				$tr_tf_el->addChild($f_el);
			}
		}

	}
	elsif($^O eq 'MSWin32')
	{
		foreach my $line (split /^/, `ipconfig /all`)
		{
			if($line =~ /\s*Physical Address(\s|\.|:)+([0-9A-F-]+)/)
			{
				my $f_el = XML::LibXML::Element->new('fact');
				$f_el->setAttribute('type', 'string');
				$f_el->setAttribute('name', 'urn:fact:ethernet:MAC');
				$f_el->appendText($2);
				$tr_tf_el->addChild($f_el);
			}
			elsif($line =~ /\s*IPv[46] Address(\s|\.|:)+([0-9.:]+)/)
			{
				my $tr_ta_el = XML::LibXML::Element->new('target-address');
				$tr_ta_el->appendText($2);
				$tr_el->addChild($tr_ta_el);
			}
		}
	}
	$tr_el->addChild($tr_tf_el);

	foreach(@selected_rules)
	{
		my $rr_el = XML::LibXML::Element->new('rule-result');
		$rr_el->setAttribute('idref', $_);
		$rr_el->setAttribute('time', $::rules{$_}{'time'});
		$rr_el->setAttribute('version', $::rules{$_}{'version'});
		
		$rr_el->appendTextChild('result', $::rules{$_}{'result'});

		if(exists($::rules{$_}{'message'}))
		{
			$rr_el->appendTextChild('message', $::rules{$_}{'message'});
		}
		$rr_el->appendTextChild('check', $::rules{$_}{'check'});
		$tr_el->addChild($rr_el);
	}

	print $xccdf_doc->toString(1);

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
