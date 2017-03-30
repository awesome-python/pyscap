#!/bin/bash

if [[ ! -d /usr/local/uvscan || ! -f /usr/local/uvscan/uvscan ]]; then
	echo Installing uvscan...
	oldir=`pwd`
	cd fix/RHEL_6_STIG/CM-173262-vscl-l64-604-l
	sh ./install-uvscan -y /usr/local/uvscan
	cd "$oldir"
else
	echo uvscan is installed
fi

echo Updating virus definitions...
unzip -o -d /usr/local/uvscan fix/RHEL_6_STIG/avvdat-*.zip

if [[ -f /etc/cron.daily/uvscan ]]; then
	echo uvscan crontab already exists
else
	echo Creating uvscan crontab...
	echo '#!/bin/sh

/usr/local/bin/uvscan --config /etc/uvscan-daily.conf / >/dev/null 2>&1
EXITVALUE=$?
if [ $EXITVALUE != 0 ]; then
    /usr/bin/logger -t uvscan "ALERT exited abnormally with [$EXITVALUE]"
fi
exit 0' > /etc/cron.daily/uvscan
	chmod 755 /etc/cron.daily/uvscan
fi

if [[ -f /etc/uvscan-daily.conf ]]; then
	echo uvscan daily config file already exists
else
	echo 'Creating uvscan daily config file...'
	echo '--afc 64
--analyze
--atime-preserve
--decompress
--mailbox
--mime
--recursive
--unzip
--xmlpath /var/log/uvscan.report
--clean' > /etc/uvscan-daily.conf
fi

if [[ -f /etc/logrotate.d/uvscan ]]; then
	echo uvscan logrotate config already exists
else
	echo 'Creating logrotate config for daily scan reports...'
	echo '/var/log/uvscan.report {
	rotate 7
	daily
	compress
	missingok
	notifempty
	create 0600 root root
}' > /etc/logrotate.d/uvscan
fi
