#!/bin/bash

find / -xdev -type f -perm -4000 -o -perm -2000 2>/dev/null | perl -e '
while(<>)
{
	chomp;
	if(`grep $_ /etc/audit/audit.rules` eq "")
	{
		print "<result>fail</result><message>setuid program not being audited: $_</message>\n";
		exit;
	}
}
print "<result>pass</result>\n";
'