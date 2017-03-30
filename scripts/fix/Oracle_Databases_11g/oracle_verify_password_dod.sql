Rem This script was modified from the Oracle utlpwdmg.sql default script.
Rem
-- This script sets the default password resource parameters.
-- This script needs to be run to enable the password features.
-- However, the default resource parameters can be changed based on the need.
-- A default password complexity function is also provided.
-- This function makes the minimum complexity checks like the minimum
-- length of the password, password not same as the username, etc. The user may
-- enhance this function according to the need.
-- This function must be created in SYS schema:
-- connect sys/<password> as sysdba before running the script
CREATE OR REPLACE FUNCTION verify_password_dod
(username varchar2,
password varchar2,
old_password varchar2)
RETURN boolean IS
n boolean;
m integer;
differ integer;
isdigit boolean;
numdigit integer;
ispunct boolean;
numpunct integer;
islowchar boolean;
numlowchar integer;
isupchar boolean;
numupchar integer;
digitarray varchar2(10);
punctarray varchar2(25);
lowchararray varchar2(26);
upchararray varchar2(26);
pw_change_time date;
BEGIN
	digitarray:='0123456789';
	lowchararray:='abcdefghijklmnopqrstuvwxyz';
	upchararray:='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
	punctarray:='@!"#$%&()``*+,-/:;<=>?_';
	-- Check if the password is same as the username
	if nls_lower(password)=nls_lower(username) then
		raise_application_error(-20001, 'Password same as or similar to user');
	end if;
	-- Check for the minimum length of the password
	if length(password) < 15 then
		raise_application_error(-20002, 'Password length less than 15');
	end if;
	-- Check if the password is too simple. A dictionary of words may be maintained
	-- and a check may be made so as not to allow the words that are too simple for
	-- the password.
	if nls_lower(password) in
	('welcome','database','account','user','password','oracle','computer','abcdefgh',
	'12345') then
		raise_application_error(-20002, 'Password too simple');
	end if;
	-- Check if the password contains at least two each of the following:
	-- uppercase characters, lowercase characters, digits and special characters.
	-- 1. Check for the digits
	isdigit:=FALSE;
	numdigit:=0;
	m:=length(password);
	for i in 1..10 loop
		for j in 1..m loop
			if substr(password,j,1)=substr(digitarray,i,1) then
				numdigit:=numdigit + 1;
			end if;
			if numdigit > 1 then
				isdigit:=TRUE;
				goto findlowchar;
			end if;
		end loop;
	end loop;
	if isdigit=FALSE then
		raise_application_error(-20003, 'Password should contain at least two digits');
	end if;
	-- 2. Check for the lowercase characters
	<<findlowchar>>
	islowchar:=FALSE;
	numlowchar:=0;
	m:=length(password);
	for i in 1..length(lowchararray) loop
		for j in 1..m loop
			if substr(password,j,1)=substr(lowchararray,i,1) then
				numlowchar:=numlowchar + 1;
			end if;
			if numlowchar > 1 then
				islowchar:=TRUE;
				goto findupchar;
			end if;
		end loop;
	end loop;
	if islowchar=FALSE then
		raise_application_error(-20003, 'Password should contain at least two lowercase characters');
	end if;
	-- 3. Check for the UPPERCASE characters
	<<findupchar>>
	isupchar:=FALSE;
	numupchar:=0;
	m:=length(password);
	for i in 1..length(upchararray) loop
		for j in 1..m loop
			if substr(password,j,1)=substr(upchararray,i,1) then
				numupchar:=numupchar + 1;
			end if;
			if numupchar > 1 then
				isupchar:=TRUE;
				goto findpunct;
			end if;
		end loop;
	end loop;
	if isupchar=FALSE then
		raise_application_error(-20003, 'Password should contain at least two uppercase characters');
	end if;
	-- 4. Check for the punctuation
	<<findpunct>>
	ispunct:=FALSE;
	numpunct:=0;
	m:=length(password);
	for i in 1..length(punctarray) loop
		for j in 1..m loop
			if substr(password,j,1)=substr(punctarray,i,1) then
				numpunct:=numpunct + 1;
			end if;
			if numpunct > 1 then
				ispunct:=TRUE;
				goto endsearch;
			end if;
		end loop;
	end loop;
	if ispunct=FALSE then
		raise_application_error(-20003, 'Password should contain at least two punctuation characters');
	end if;
	-- Check if the password differs from the previous password
	-- by more than 4 characters
	<<endsearch>>
	if old_password is not null then
		differ:=length(old_password) - length(password);
		if abs(differ) < 4 then
			if length(password) < length(old_password) then
				m:=length(password);
			else
				m:=length(old_password);
			end if;
			differ:=abs(differ);
			for i in 1..m loop
				if substr(password,i,1) != substr(old_password,i,1) then
					differ:=differ + 1;
				end if;
			end loop;
			if differ < 4 then
				raise_application_error(-20004, 'Password should differ by more than 4 characters');
			end if;
		end if;
	end if;
	-- Everything is fine. return TRUE
	RETURN(TRUE);
	EXCEPTION
	WHEN OTHERS THEN
	raise_application_error(-20000,'verify_password_dod: Unexpected error: '||SQLERRM,TRUE);
END;
/
alter profile default limit
password_verify_function verify_password_dod;
EXIT