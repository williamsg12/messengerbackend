drop database messenger;
drop user messengeruser;


create database messenger;
create user messengeruser with password 'messenger';
GRANT ALL PRIVILEGES ON DATABASE messenger TO messengeruser;