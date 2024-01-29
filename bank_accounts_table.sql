create database bank;
use bank;

create table accounts(
AccountNumber int not null,
passward varchar(100) not null,
name varchar(50) not null,
gender char(1) not null,
balence int not null ,
age int not null,
primary key (AccountNumber)
);
