create table if not exists User (
 user_id int primary key,
 name Varchar (50) not null,
 father_Name Varchar (50) not null,
 aadhaar_number bigint not null unique,
 dob date not null,
 contact bigint not null,
 email varchar (50) not null,
 city varchar (20) not null,
 passwd varchar (100) not null,
 gender varchar(7) not null
);

create table if not exists Role (
 user_id int not null,
 role_id int not null,
 foreign key (user_id) references User(user_id)
);

create table if not exists Approval (
 user_id int not null,
 is_approved bool not null,
 foreign key (user_id) references user(user_id)
);

create table if not exists VoteRecord (
user_id int not null,
status bool not null,
vote_id int not null,
foreign key (user_id) references user(user_id)
);

create table if not exists Party (
 party_id int not null primary key,
 party_name varchar(50) not null unique
);

create table if not exists Result(
party_id int not null,
election_year int not null,
votes int not null,
primary key(party_id,election_year),
foreign key (party_id) references Party(party_id)
);

create table if not exists Election_Year (
 year int not null primary key,
 status int not null
); 