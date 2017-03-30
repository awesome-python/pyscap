#!/bin/bash

echo -n "This fix flushes the IPv4 INPUT chain's rules, so if you are remotely connected, you may not want to risk this (y/n): [n]"
read r
if [[ "$r" != "y" ]]; then
	exit
fi

f=/etc/sysconfig/iptables
if [[ -f $f ]]; then
	. lib/file.sh
backup_file $f || exit 1
fi

echo Flushing INPUT chain...
iptables -F INPUT

echo Allowing established traffic...
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

echo Allowing ping requests and destination unreachable messages...
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp --icmp-type destination-unreachable -j ACCEPT

echo Allowing traffic from localhost but only through the lo interface...
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT ! -i lo -s 127.0.0.0/8 -j DROP

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
	
	# skip ipv6
	next if $laddr =~ /:/;
	
	# skip localhost (already covered by lo rule)
	next if $laddr eq "127.0.0.1";
	
	if($laddr eq "0.0.0.0")
	{
		`iptables -A INPUT -p $proto --dport $lport -j ACCEPT`
	}
	else
	{
		`iptables -A INPUT -d $laddr -p $proto --dport $lport -j ACCEPT`
	}
}
'

echo Setting default policy to DROP packets...
iptables -P INPUT DROP

echo Saving changes to $f.
iptables-save > $f