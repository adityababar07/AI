create database ai;
create table ai_account(
id int auto_increment primary key,
username varchar(20) not null,
name varchar(100) not null,
password varchar(64) not null,
email varchar(20),
age int
);

insert into ai.ai_account values("hacker07", "aditya", "nidhi@149489", "avia00700@gmail.com", 17);

