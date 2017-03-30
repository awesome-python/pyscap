#!/bin/bash

. lib/mysql.sh

r=`mysql -s -N -e "SHOW VARIABLES LIKE 'old_passwords'"`
if [[ "x$r" == "x" ]]; then
	echo '<result>fail</result>'
	exit
fi

# check we're using strong passwords
get_mysql_option mysqld default_authentication_plugin
if [[ -z "$result" || "x$result" != "xsha256_password" ]]; then
	echo '<result>fail</result>'
	exit
fi

exit

# TODO Variables
#interactive_timeout
#wait_timeout
#max_user_connections
#old_passwords
#secure_auth
#secure_file_priv
#sql_log_off
#automatic_sp_privileges
#expire_logs_days
#have_symlink

# TODO config
# Disable or restrict remote access
#skip-networking
#bind-address=127.0.0.1

# Disable the use of LOCAL INFILE
#set-variable=local-infile=0

# Change root username and password
#RENAME USER root TO new_user;
#SET PASSWORD FOR 'username'@'%hostname' = PASSWORD('newpass');

# Remove the "test" database
#drop database test;
#delete from mysql.db; 

# Remove Anonymous and obsolete accounts
#select * from mysql.user where user="";
#DROP USER ""
# remove everything except root
#delete from mysql.user where not (host="localhost" and user="root");
#flush privileges;

# Lower system privileges
#ls -l /var/lib/mysql
#chown -R mysql.mysql /var/lib/mysql
#ls -l /usr/bin/my*
#chown mysql.mysql /usr/bin/my*
#chmod 755 /usr/bin/my*

### Lower database privileges
# Operating system permissions were fixed in the preceding section. Now let’s talk about database permissions. In most cases, there is an administrator user (the renamed "root") and one or more actual users who coexist in the database. Usually, the "root" has nothing to do with the data in the database; instead, it is used to maintain the server and its tables, to give and revoke permissions, etc.

# On the other hand, some user ids are used to access the data, such as the user id assigned to the web server to execute "select\update\insert\delete" queries and to execute stored procedures. In most cases, no other users are necessary; however, only you, as a system administrator can really know your application’s needs.

# Only administrator accounts need to be granted the SUPER / PROCESS /FILE privileges and access to the mysql database. Usually, it is a good idea to lower the administrator’s permissions for accessing the data.

# Review the privileges of the rest of the users and ensure that these are set appropriately. This can be done using the following steps.

# mysql> use mysql;

# [Identify users]

# mysql> select * from users;

# [List grants of all users]

# mysql> show grants for ‘root’@’localhost’;

# The above statement has to be executed for each user ! Note that only users who really need root privileges should be granted them.

# Another interesting privilege is "SHOW DATABASES". By default, the command can be used by everyone having access to the MySQL prompt. They can use it to gather information (e.g., getting database names) before attacking the database by, for instance, stealing the data. To prevent this, it is recommended that you follow the procedures described below.

# Add " --skip-show-database" to the startup script of MySQL or add it to the MySQL configuration file
# Grant the SHOW DATABASES privilege only to the users you want to use this command
# To disable the usage of the "SHOW DATABASES" command, the following parameter should be added in the [mysqld] section of the /etc/my.cnf:

# [mysqld]
# skip-show-database
### Enable Logging

# If your database server does not execute many queries, it is recommended that you enable transaction logging, by adding the following line to [mysqld] section of the /etc/my.cnf file:

# [mysqld]
# log =/var/log/mylogfile

# This is not recommended for heavy production MySQL servers because it causes high overhead on the server.

# In addition, verify that only the "root" and "mysql" ids have access to these logfiles (at least write access).

# Error log

# Ensure only "root" and "mysql" have access to the logfile "hostname.err". The file is stored in the mysql data directory. This file contains very sensitive information such as passwords, addresses, table names, stored procedure names and code parts. It can be used for information gathering, and in some cases, can provide the attacker with the information needed to exploit the database, the machine on which the database is installed, or the data inside it.

# MySQL log

# Ensure only "root" and "mysql" have access to the logfile "*logfileXY". The file is stored in the mysql data directory.

### Change the root directory

# A chroot on Unix operating systems is an operation that changes the apparent disk root directory for the current running process and its children. A program that is re-rooted to another directory cannot access or name files outside that directory, and the directory is called a "chroot jail" or (less commonly) a "chroot prison".

# By using the chroot environment, the write access of the MYSQL processes (and child processes) can be limited, increasing the security of the server.

# Ensure that a dedicated directory exists for the chrooted environment. This should be something like:/chroot/mysqlIn addition, to make the use of the database administrative tools convenient, the following parameter should be changed in the [client] section of MySQL configuration file:

# [client]
# socket = /chroot/mysql/tmp/mysql.sock

# Thanks to that line of code, there will be no need to supply the mysql, mysqladmin, mysqldump etc. commands with the --socket=/chroot/mysql/tmp/mysql.sock parameter every time these tools are run.

#### Remove History

# During the installation procedures, there is a lot of sensitive information that can assist an intruder to assault a database. This information is stored in the server’s history and can be very helpful if something goes wrong during the installation. By analyzing the history files, administrators can figure out what has gone wrong and probably fix things up. However, these files are not needed after installation is complete.

# We should remove the content of the MySQL history file (~/.mysql_history), where all executed SQL commands are stored (especially passwords, which are stored as plain text):

# cat /dev/null > ~/.mysql_history

### Patch your systems

# Consult you operation system’s vendor for security and performance updates: use windows update on windows, apt-get or yum on (Debian) systems, Red Hat update Agent on Red hat and so on.

# Windows : http://www.windowsupdate.com/

# Redhat : http://www.redhat.com/docs/manuals/RHNetwork/ref-guide/3.6/ch-up2date.html

# Debian: http://www.cyberciti.biz/faq/rhel-centos-fedora-linux-yum-command-howto/ orhttps://help.ubuntu.com/8.04/serverguide/C/apt-get.html

# MacOS: http://support.apple.com/kb/HT1338

 

# If you are using any kind of virtualization platform, consult your platform vendor for security issues, patches and recommendations.