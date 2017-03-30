#!/bin/bash

echo -n "This fix flushes the IPv6 INPUT chain's rules, so if you are remotely connected, you may not want to risk this (y/n): [n]"
read r
if [[ "$r" != "y" ]]; then
	exit
fi

f=/etc/sysconfig/ip6tables
if [[ -f $f ]]; then
	. lib/file.sh
backup_file $f || exit 1
fi

echo Flushing INPUT chain...
ip6tables -F INPUT

echo Allowing established traffic...
ip6tables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

echo Allowing ping requests and destination unreachable messages...
ip6tables -A INPUT -p icmpv6 --icmpv6-type echo-request -j ACCEPT
ip6tables -A INPUT -p icmpv6 --icmpv6-type destination-unreachable -j ACCEPT

echo Allowing traffic from localhost but only through the lo interface...
ip6tables -A INPUT -i lo -j ACCEPT
ip6tables -A INPUT ! -i lo -s ::1 -j DROP

echo Allowing all public listening sockets in netstat...
netstat -lutn | perl -e '
# skip first two lines
<>;
<>;
while(<>)
{
	/^(tcp|udp)\s+[0-9+\s+[0-9]+\s+([0-9:.]+):([0-9]+)/;
	my $proto = $1;
	my $laddr = $2;
	my $lport = $3;
	
	# skip ipv4
	next if $laddr =~ /\./;
	
	# skip localhost (already covered by lo rule)
	next if $laddr eq "::1";
	
	if($laddr eq "::")
	{
		`ip6tables -A INPUT -p $proto --dport $lport -j ACCEPT`
		print "ACCEPTing Protocol: $proto Address: $laddr Port: $lport\n";
	}
	else
	{
		`ip6tables -A INPUT -d $laddr -p $proto --dport $lport -j ACCEPT`
		print "ACCEPTing Protocol: $proto Address: $laddr Port: $lport\n";
	}
}
'

echo Setting default policy to DROP packets...
ip6tables -P INPUT DROP

echo Saving changes to $f.
ip6tables-save > $f