#!/bin/bash

# this is the audit.rules super fix
# add & uncomment the following line to files that change audit.rules and add their fixes below
#sh fix/RHEL_6_STIG/audit_rules.sh || exit 1

f=/etc/audit/audit.rules
. lib/file.sh
backup_file $f || exit 1

r=`grep STIG_RHEL_6 $f`
if [[ "x$r" != "x" ]]; then
	echo "AUDIT RULES ALREADY ADDED!!!"
	exit 1
fi

uname_i=`uname -i`

if [[ $uname_i == "x86_64" ]]; then
	archs="b32 b64"
else
	archs='b32'
fi

function audit_system_call {
	if [[ "x$1" == "x" || "x$2" == "x" ]]; then
		echo "Usage: audit_system_call system_call key"
		exit 1
	fi
	
	for arch in $archs; do
		echo "-a always,exit -F arch=$arch -S $1 -F auid>=500 -F auid!=4294967295 -k $2"
		echo "-a always,exit -F arch=$arch -S $1 -F auid=0 -k $2"
	done
}

echo '' >> $f
echo '### STIG_RHEL_6 rules' >> $f
echo '' >> $f
echo '# STIG audit_time_rules' >> $f
echo "-a always,exit -F arch=b32 -S settimeofday -k audit_time_rules" >> $f
if [[ $uname_i == "x86_64" ]]; then
	echo "-a always,exit -F arch=b64 -S settimeofday -k audit_time_rules" >> $f
fi
echo "-a always,exit -F arch=b32 -S stime -k audit_time_rules" >> $f
# not needed on 64 bit
echo "-a always,exit -F arch=b32 -S clock_settime -k audit_time_rules" >> $f
if [[ $uname_i == "x86_64" ]]; then
	echo "-a always,exit -F arch=b64 -S clock_settime -k audit_time_rules" >> $f
fi
echo '-w /etc/localtime -p wa -k audit_time_rules' >> $f
echo "-a always,exit -F arch=b32 -S adjtimex -k audit_time_rules" >> $f
if [[ $uname_i == "x86_64" ]]; then
	echo "-a always,exit -F arch=b64 -S adjtimex -k audit_time_rules" >> $f
fi

echo '' >> $f
echo '# STIG audit_account_changes' >> $f
echo '-w /etc/group -p wa -k audit_account_changes' >> $f
echo '-w /etc/passwd -p wa -k audit_account_changes' >> $f
echo '-w /etc/gshadow -p wa -k audit_account_changes' >> $f
echo '-w /etc/shadow -p wa -k audit_account_changes' >> $f
echo '-w /etc/security/opasswd -p wa -k audit_account_changes' >> $f

echo '' >> $f
echo '# STIG audit_network_modifications' >> $f
echo "-a exit,always -F arch=b32 -S sethostname -S setdomainname -k audit_network_modifications" >> $f
if [[ $uname_i == "x86_64" ]]; then
	echo "-a exit,always -F arch=b64 -S sethostname -S setdomainname -k audit_network_modifications" >> $f
fi
echo '-w /etc/issue -p wa -k audit_network_modifications' >> $f
echo '-w /etc/issue.net -p wa -k audit_network_modifications' >> $f
echo '-w /etc/hosts -p wa -k audit_network_modifications' >> $f
echo '-w /etc/sysconfig/network -p wa -k audit_network_modifications' >> $f

echo '' >> $f
echo '# STIG MAC-policy' >> $f
echo '-w /etc/selinux/ -p wa -k MAC-policy' >> $f

echo '' >> $f
echo '# STIG perm_mod' >> $f
audit_system_call 'chown' 'perm_mod' >> $f
audit_system_call 'fchmod' 'perm_mod' >> $f
audit_system_call 'fchmodat' 'perm_mod' >> $f
audit_system_call 'fchown' 'perm_mod' >> $f
audit_system_call 'fchownat' 'perm_mod' >> $f
audit_system_call 'fremovexattr' 'perm_mod' >> $f
audit_system_call 'fsetxattr' 'perm_mod' >> $f
audit_system_call 'lchown' 'perm_mod' >> $f
audit_system_call 'lremovexattr' 'perm_mod' >> $f
audit_system_call 'lsetxattr' 'perm_mod' >> $f
audit_system_call 'removexattr' 'perm_mod' >> $f


echo '' >> $f
echo '# STIG access' >> $f
for ARCH in $archs; do
	echo "-a always,exit -F arch=$ARCH -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid>=500 -F auid!=4294967295 -k access" >> $f
	echo "-a always,exit -F arch=$ARCH -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid>=500 -F auid!=4294967295 -k access" >> $f
	echo "-a always,exit -F arch=$ARCH -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EACCES -F auid=0 -k access" >> $f
	echo "-a always,exit -F arch=$ARCH -S creat -S open -S openat -S truncate -S ftruncate -F exit=-EPERM -F auid=0 -k access" >> $f
done

echo '' >> $f
echo '# STIG privileged' >> $f
for setuid_f in `find / -xdev -type f -perm -4000 -o -perm -2000 2>/dev/null`; do
	echo Checking for existing audit rule for $setuid_f
	r=`grep $setuid_f $f`
	if [[ "x$r" == "x" ]]; then
		echo "Didn't find audit rule for $setuid_f, adding..."
		echo "-a always,exit -F path=$setuid_f -F perm=x -F auid>=500 -F auid!=4294967295 -k privileged" >> $f
	fi
done

echo '' >> $f
echo '# STIG export' >> $f
audit_system_call 'mount' 'export' >> $f

echo '' >> $f
echo '# STIG delete' >> $f
for arch in $archs; do
	echo "-a always,exit -F arch=$arch -S unlink -S unlinkat -S rename -S renameat -F auid>=500 -F auid!=4294967295 -k delete" >> $f
	echo "-a always,exit -F arch=$arch -S unlink -S unlinkat -S rename -S renameat -F auid=0 -k delete" >> $f
done

echo '' >> $f
echo '# STIG actions' >> $f
echo '-w /etc/sudoers -p wa -k actions' >> $f

echo '' >> $f
echo '# STIG modules' >> $f
echo '-w /sbin/insmod  -p x -k modules' >> $f
echo '-w /sbin/rmmod  -p x -k modules' >> $f
echo '-w /sbin/modprobe  -p x -k modules' >> $f
for arch in $archs; do
	echo "-a always,exit -F arch=$arch -S init_module -S delete_module -k modules" >> $f
done

service auditd restart
sleep 5s